class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        table = [[0 for _ in range(len(p))] for j in range(len(s))]
        table[0][0] = 1

        for i in range(1, len(p)):
            if p[i] == "*":
                table[0][i] = table[0][i - 2]

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == "." or p[i] == s[j]:
                    table[j][i] = table[j - 1][i - 1]
                elif p[i] == "*":
                    table[j][i] = table[j][i - 2] or int(table[j - 1][i] and (p[i - 1] == s[j] or p[i - 1] == "."))

        return bool(table[-1][-1])

a = Solution()
print(a.isMatch("ab", ".*"))

#https://leetcode.com/problems/regular-expression-matching/submissions/1083167565/


