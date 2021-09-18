# Depth First Search

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

visited = [False]*9
dfs(graph, 1, visited)