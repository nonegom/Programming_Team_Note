# 서로소 집합 경로 압축 기법
    # 각 원소가 속한 집합이 부모 테이블의 값과 같아진다.


# 루트노드가 아니라면 루트노드를 찾을 때까지 재귀적 호출
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]

""" 
서로소 집합 경로 기본 기법
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x]) <- 해당 부분 차이
    return parent[x]
"""

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
#########################

# vertex, edge
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(v+1):
    parent[i] = i

# union 연산을 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = " ")
for i in range(1, v+1):
    print(find_parent(parent, i), end = " ")
print()
print("부모 테이블: ", end = " ")
for i in range(1, v+1):
    print(parent[i], end = " ")
