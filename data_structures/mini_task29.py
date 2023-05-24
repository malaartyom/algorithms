def list_minus(list1, list2):
    return list(set(list1) - set(list2))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = list()
    visited.append(start)

    for next in list_minus(graph[start], visited):
        dfs(graph, next, visited)
    return visited
