# 서로소 집합 사이클 판별

def find_parent(parent, x):
    if parent[x] != x: # 루트노드가 아니라면 루트노드를 찾을 때까지 재귀적 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# vertex, edges    
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
if cycle:
    print("cycle이 발생")
else:
    print("cycle이 발생하지 않음")