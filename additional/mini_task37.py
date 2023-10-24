class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        n_row, n_col = len(dungeon), len(dungeon[0])
        hp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        get_req_hp = lambda acc: 1 - acc if acc < 0 else 1
        hp[-1][-1] = get_req_hp(dungeon[-1][-1])
        for c in range(n_col-2, -1, -1):
            hp[-1][c] = max(hp[-1][c+1] - dungeon[-1][c], 1)
        for r in range(n_row-2, -1, -1):
            hp[r][-1] = max(hp[r+1][-1] - dungeon[r][-1], 1)
        for r in range(n_row-2, -1, -1):
            for c in range(n_col-2, -1, -1):
                l_hp = max(hp[r][c+1] - dungeon[r][c], 1)
                u_hp = max(hp[r+1][c] - dungeon[r][c], 1)
                hp[r][c] = min(u_hp, l_hp)
        return hp[0][0]

print(Solution.calculateMinimumHP(Solution, [[-2,-3,3],[-5,-10,1],[10,30,-5]]))