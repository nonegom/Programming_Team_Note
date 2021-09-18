# Breadth First Search

from collections import deque

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

def bfs(graph, start, visited):
    visited[start] = True
    deq = deque([start])
    while deq:
        v = deq.popleft()
        print(v, end=" ") # 출력은 pop할 떄
        for i in graph[v]:
            if not visited[i]:
                deq.append(i) # append 시킬 때 확인 처리를 해줘야 한다.
                visited[i] = True
                
visited = [False]*9
bfs(graph, 1, visited)