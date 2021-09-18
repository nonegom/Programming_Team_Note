"""
# heapq
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용한다.
- `heapq.heappush(list, value)`, `heapq.heappop(list)` 두 가지 메소드만 알아도 충분히 구현 가능
- 기본적으로 숫자가 낮은값이 먼저 나오기 (오름차순) 때문에 높은 값을 먼저 나오게 하기 위해서는 `-`를 붙이는 방법을 사용한다.
"""

import heapq

def heapsort(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

## 내림차순 heapq
def reverse_heapsort(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result2 = reverse_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result2)