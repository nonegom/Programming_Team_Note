# 위상 정렬
## 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘
## 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열

from collections import deque

v,e = map(int, input().split())
indegree= [0] * (v+1)
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동가능    
    indegree[b] += 1   # 진입차수를 1증가
    
# 위상 정렬함수
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌 때 까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")
        
topology_sort()