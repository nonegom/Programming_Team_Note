# 구간 합 계산
## 여러 번 사용될 만한 정보는 미리 구해 저장해 놓는다.
## 결국 구간의 합이라는 것은 $P[R] - P[L-1]$이 된다.
# 다이나믹 프로그래밍과 유사

n = 5
data = [10, 20, 30, 40, 50]
left = 3
right = 4

def partition_sum(left, right):
    sum_list = [0] # 0을 넣어줘야 0번째 자리가 찬다. 그래서 다음부터 1로 연산을 할 수가 있다.
    sum_value = 0
    for i in data:
        sum_value += i
        sum_list.append(sum_value)
    return sum_list[right] - sum_list[left-1]

partition_sum(left, right)