from typing import List
import math

def print_A(A):
    for i in A:
        for j in i:
            print(j)
        print()
class Solution:
    @staticmethod
    def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        A = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        E = dict()

        for edge in edges:
            E[(edge[0], edge[1])] = edge[2]
            E[(edge[1], edge[0])] = edge[2]
            

        for i in range(n):
            for j in range(n):
                if i == j:
                    A[i][j][0] = 0
                elif (i, j) in E.keys():
                    A[i][j][0] = E[(i, j)]
                else:
                    A[i][j][0] = math.inf

        for k in range(1, n):
            for i in range(1, n):
                for j in range(1, n):
                    A[i][j][k] = min(A[i][j][k - 1], A[i][k][k - 1] + A[k][j][k - 1])

        k = math.inf
        answ = []
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and A[i][j][-1] <= distanceThreshold:
                    count += 1

            if k >= count:
                k = count
                answ.append(i)

        return answ

        





n = 4
edges = [[0,1,3977],[2,3,8807],[0,2,2142],[1,3,1201]]
distanceThreshold = 8174
print(Solution.findTheCity(n, edges, distanceThreshold))



