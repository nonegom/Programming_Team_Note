# 공식을 기억하고 있어야 한다.

# 시계방향
def rotate_matrix_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            print((i, j), (j, n-i-1))
            result[j][n-i-1] = a[i][j]
    return result

# 반 시계방향
def rotate_matrix_90_degree_reverse(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            print((i, j), (j, n-i-1))
            result[i][j] = a[j][n-i-1]
    return result

## 파이썬으로 넘파이 없이 회전하기
"""
- zip의 성질을 활용한 코드
- *를 통해 reverse한 연산을 빼주고 zip연산을 통해 묶음으로써 90도 돌게 되는 효과를 받을 수 있다.
- 90도, 180도만 보고 270도는 그냥 90도 변환후 180도 변환을 연이어서 진행
"""
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

krots = [
    key,                                                                        # 0도, 기본
    list(zip(*reversed(key))),                                                  #90도, 회전
    list(map(lambda e:list(reversed(e)), reversed(key))),                       #180도, 회전
    list(map(lambda e:list(reversed(e)), reversed(list(zip(*reversed(key)))))), #270도, 회전
]