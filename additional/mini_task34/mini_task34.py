class Union_find:

    def __init__(self, N) -> None:
        self.verts = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def __str__(self) -> str:
        return (f"Verts: {self.verts}")+ "\n" + (f"Rank:  {self.rank}") + "\n" + (f"Size:  {self.rank}")
    
    def get_verts(self):
        return self.verts
        

    def union(self, x, y):
        # a = self.find(x)
        # b = self.find(y)
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
    
U = Union_find(5)


def solution(data: str) -> (int, int):
    data = [list(map(int, i.split())) for i in data.splitlines()]
    N = data[0][0]
    _M = data[0][1]
    route_couter = 0
    data = sorted(data[1:], key=lambda x: x[2])
    union = Union_find(N)
    help_set = set()
    for rib in data:
        a = union.find(rib[0])
        b = union.find(rib[1])
        if a != b:
            union.union(a, b)
            route_couter += rib[2]

    for vert in union.get_verts():
        help_set.add(union.find(vert))
    

    return (len(help_set), route_couter)
    