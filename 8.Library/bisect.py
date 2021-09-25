"""
# bisect
- 이진 탐색을 쉽게 구현할 수 있는 라이브러리
- bisect_left(), bisect_right() 함수
- 이를 활용해 정렬된 리스트에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 수 있음
"""
from bisect import bisect_left, bisect_right

a = [1,2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

print("============")
# bisect 활용: 정렬된 위치에서 [left_value, right_value]에 속하는 데이터의 개수를 반환
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(b, 4, 4)) # 값이 4인 데이터 개수 출력
print(count_by_range(b, -1, 3)) # 값이 -1과 3사이의 데이터 개수 출력 