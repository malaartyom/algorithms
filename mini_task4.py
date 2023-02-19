import os
import subprocess as sb

def git_bisect(pathname, start, end, command):
    pathname = os.path.abspath(pathname)
    os.chdir(pathname)
    if len(start) < 40:
        format = "%h"
    else:
        format = "%H"
    commits = [i.decode().strip('"') for i in \
          sb.run(['git', 'log', f'--format="{format}"'], capture_output=True).stdout.splitlines()][::-1]
    l = commits.index(start)
    r = commits.index(end)
    while l <= r:
        pivot = (l + r) // 2
        sb.run(['git', 'checkout', commits[pivot], '-q'], capture_output=True)
        pivot_exit = sb.run(command, capture_output=True).returncode
        sb.run(['git', 'checkout', commits[pivot - 1], '-q'],  capture_output=True)
        pivot_exit_minus1 = sb.run(command, capture_output=True).returncode
        if pivot_exit != 0 and pivot_exit_minus1 == 0:
            return commits[pivot]
        elif pivot_exit == 0:
            l = pivot + 1
        elif pivot_exit != 0 and pivot_exit_minus1 != 0:
            r = pivot - 1
    sb.run(['git', 'checkout', 'main', '-q'], capture_output=True)


s = '096e212f4dbeb16018e2fb5284635f38a17cf308'
e = 'cc5128770cbef8c0d4b7e88fcf84a3764c1f782b'
sb.run(['git', 'checkout', 'main', '-q'], capture_output=True, cwd=os.path.abspath("/Users/artemmalarenko/Documents/GitHub/test_for_git_bisect"))
com = ["Python3", "test.py"]
try:
    print(git_bisect("/Users/artemmalarenko/Documents/GitHub/test_for_git_bisect", s, e, com))
finally:
    sb.run(['git', 'checkout', 'main', '-q'], capture_output=True, cwd=os.path.abspath("/Users/artemmalarenko/Documents/GitHub/test_for_git_bisect"))

