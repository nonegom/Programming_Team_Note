# Programming_Team_Note

- This repository is a python library for PS(Problem-Solving) Competition
- 코딩 테스트를 위한 알고리즘 노트입니다. (출처: 이것이 코딩테스트다(나동빈 저 ))

# Algorithm

## 1. DFS & BFS

- [DFS](/1. DFS&BFS/DFS)
- [BFS](/1. DFS&BFS/BFS)

## 2. Sorting (정렬)

* [Selection Sort](/2. Sorting/selection_sort.py)
* [Insertion Sort](/2. Sorting/insertion_sort.py)
* [Quick Sort](//2. Sorting/quick_sort.py)
* [Counting Sort](//2. Sorting/counting_sort.py)
* [Python Sort Library](/2. Sorting/python_sort_library.py)

## 3. Searching (탐색)

- [Binary Search](/Algorithm/3.Searching\BinarySearch.py)

## 4. Dynamic Programming (동적 프로그래밍)

- [DynamicProgramming](Algorithm\4. Dynamic Programming\DynamicProgramming.py)

## 5. Shortest path (최단경로)

## 6. Graph Theory (그래프 이론)

## 7. Algorithm Theory (기타 알고리즘)

## 8. Function ( 함수) 

# Comments

## 1.  Greedy  (그리디)

 그리디 알고리즘은 주어진 상황에서 가장 최선의 선택을 하는 알고리즘이다. 장기적으로 보면 더 나은 결과를 도출할 수도 있겠지만 현재 가장 좋아보이는 판단을 한다. 구현이 가장 간단하다는 장점이 있다.

## 2. Realization (구현)

 구현 문제의 경우 떠올리는 아이디어는 쉽지만 그것을 코드로 만들기에 어려운 문제들을 구현 문제라고 한다.

## 3. DFS & BFS

 DFS는 깊이 우선탐색이라고 하고, BFS는 너비 우선 탐색이라고 한다.

- DFS: 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 인접행렬과 인접 리스트 방식이 존재한다. 데이터의 개수가 N개인 경우 $O(N)$의 시간이 소요된다.
- BFS: 가까운 노드부터 먼저 탐색하는 알고리즘이다. 큐 자료구조를 이용해서 구현한다.  `deque`라이브러리를 이용하고, $O(N)$의 시간이 소요된다.

## 4. Sorting (정렬)

정렬은 기본적으로 `sort()`와 `sorted()` 함수로 구현이 가능하긴 하다. 하지만 정렬의 기본이 되는 몇 가지 행렬의 알고리즘이 있다.

- 선택정렬
- 삽입정렬
- 계수정렬
- 퀵정렬
- 정렬 라이브러리

## 5. Searching (탐색)

 탐색 중에서 이진 탐색은 정렬된 상태에서만 사용이 가능한 탐색 방법이다. 순차 탐색보다 탐색시간이 $O(\log N)$으로 줄어든다는 장점이 있다. 그래서 탐색의 범위가 매우 큰 데이터의 경우 이진 탐색으로 풀어야 하는 경우가 있다. 참고로 이진탐색을 하게해주는 라이브러리 `bisect`가 존재하기도 한다.

## 6. Dynamic Programming (동적 프로그래밍)

 다이나믹 프로그래밍은 이전의 연산을 다음 연산에 활용하게 될 경우 유용한 알고리즘이다. 가장 대표적인 예로 피보나치 수열을 들 수 있다. 점화식을 세울 수 있는 연산은 보통 Dynamic Programming으로 구현이 가능하다. 결과를 담은 리스트를 하나 생성해서 연산 기록을 남기는 방법이라고 할 수 있다.

## 7. Shortest path (최단경로)

## 8. Graph Theory (그래프 이론)

## 9. Algorithm Theory (기타 알고리즘)



# 
