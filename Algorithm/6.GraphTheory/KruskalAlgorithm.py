# 가장 적은 비용으로 모든 노드를 연결하는 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

##### 여기까지 서로소 집합과 유사하다고 할 수 있다. ######
    
# 모든 간선에 대한 정보 받기 (cost를 받는다.)
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해서 cost를 앞에 배치
     
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)