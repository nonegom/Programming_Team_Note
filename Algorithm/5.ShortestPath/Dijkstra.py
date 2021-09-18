# 노드개수, 간선개수
import heapq
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 해당 함수 코드를 외우면 된다.
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면 계속 반복
        dist, now = heapq.heappop(q) # 큐를 뽑음
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for info in graph[now]:
            cost = dist + info[1] # 거리 
            if cost < distance[info[0]]: # 노드
                distance[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY", end=" ")
    else:
        print(distance[i], end=" ")