


def is_bipartite(graph: list) -> bool:
    for i in range(len(graph)):
        graph[i] = [graph[i], 0]
    graph[0][1] = 1
    for i in range(len(graph)):
        for j in range(len(graph[i][0])):
            if graph[i][1] == 1:
                if graph[graph[i][0][j]][1] == 1:
                    return False
                else:
                    graph[graph[i][0][j]][1] = -1

            elif graph[i][1] == -1:
                if graph[graph[i][0][j]][1] == -1:
                    return False
                else:
                    graph[graph[i][0][j]][1] = 1
            elif graph[i][1] == 0:
                graph[i][1] = 1

    return True
                

a = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(is_bipartite(a))