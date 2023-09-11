from collections import List
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        for i in range(len(edges)): 
            curr = i
            path = []
            while edges[curr] >= 0: 
                path.append(curr)
                next = edges[curr]
                edges[curr] = -1  
                curr = next
            if curr in path: 
                ans = max(ans, len(path)-path.index(curr)) 
        return ans