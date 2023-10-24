class Union_find:

    def __init__(self, N) -> None:
        self.verts = list(range(N))
        self.rank = [0 for i in range(N)] 
        

    def __str__(self) -> str:
        return (f"Verts: {self.verts}")+ "\n" + (f"Rank:  {self.rank}") + "\n" + (f"Size:  {self.rank}")
    
    def get_verts(self):
        return self.verts
        

    def union(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.verts[y] = self.verts[x]
        else:
            self.verts[x] = self.verts[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
         

    def find(self, x):
        pos = x
        while self.verts[pos] != pos:
            pos = self.verts[pos]
        self.verts[x] = self.verts[pos]
        return pos
    

def solution(tasks: list((int, int))):
    tasks = sorted(tasks, key=lambda x: x[1])[::-1]
    print(tasks)
    union = Union_find(len(tasks))
    result = [-1 for _ in range(len(tasks))]
    end = []
    j = 0
    for i in tasks:
        a = union.find(i[0])
        if result[a] == -1:
            result[a] = i[2]
        else:
            if i[0] - j > 0:
                result[a - 1] = i[2]
            else:
                end.append(i[2])
        j += 1
        union.union(a, a - 1)


    return result + end

print(solution([(3, 25, 'A'), (4, 10, 'B'), (1, 30, 'C'), (3, 50, 'D'), (3, 20, 'E')]))

    

