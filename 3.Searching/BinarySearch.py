# Binary Search는 재귀적인 방법과 반목문을 활용한 방법 2개가 가능하다.

n, target = 3, 2
array = [1, 4, 5]

## 재귀적 풀이 1
def binary_search(array, start, end, target):
    mid = (start+end) // 2
    if start > end:
        return None
    elif array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid+1, end, target)
    else:
        return binary_search(array, start, mid-1, target)

result = binary_search(array, 0, n-1, target)
if result == None:
    print("찾을 수 없음")
else:
    print(result+1)

# 반복문 풀이 2
def binarysearch_for(array, target, start, end):
    while True:
        if start > end: # 탈출
            break
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif target < array[mid]:
            end = mid-1
        elif target > array[mid]: #else로 둬도 괜찮다.
            start = mid +1

result = binarysearch_for(array, target, 0, n-1)
if result == None:
    print("찾을 수 없음")
else:
    print(result+1)