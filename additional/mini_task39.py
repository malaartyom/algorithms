class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        table = [[0 for _ in range(len(p))] for j in range(len(s))]
        table[0][0] = 1

        for i in range(1, len(p)):
            if p[i] == "*":
                table[0][i] = table[0][i - 1]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] == "?" or p[j] == s[i]:
                    table[i][j] = table[i - 1][j - 1]
                elif p[j] == "*":
                    table[i][j] = table[i][j - 1] or table[i - 1][j]


        print(table)

        return bool(table[-1][-1])
sol = Solution()
sol.isMatch()
#https://leetcode.com/problems/wildcard-matching/submissions/1083174823/

