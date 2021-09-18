## 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리한다.
# 부분합 문제나 두 개의 리스트를 합치는 문제에 사용한다.

# 부분합 문제
n = 5 # 데이터의 길이
m = 5 # 찾아야 할 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    # interval_sum이 크거나 같아지면 while문을 빠져나간다.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)


# 정렬되어 있는 두 두 리스트의 합집합 문제
n, m = 6, 4
a = [1, 3, 5, 8, 9, 11]
b = [2, 4, 6, 7]

ls = []

i = 0
j = 0

# i < n이 핵심 코드 i가 n을 넘어버린 상태면 끝도 없이 a가 증가하게 된다.
while i < n or j < m:
    if j >= m or (i< n and a[i] <= b[j]):  # and연산 앞에 뭐가 먼저 오는지도 중요
        ls.append(a[i])
        i+=1
    else:
        ls.append(b[j])
        j+=1
        
print(ls)