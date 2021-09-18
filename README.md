# Programming_Team_Note

- This repository is a python library for PS(Problem-Solving) Competition
- 코딩 테스트를 위한 알고리즘 노트입니다. (출처: 이것이 코딩테스트다(나동빈 저 ))

## Algorithm

### 1. DFS & BFS

- [DFS](Algorithm/1.DFS&BFS/DFS)
- [BFS](Algorithm/1.DFS&BFS/BFS)

### 2. Sorting (정렬)

- [Python Sort Library](Algorithm/2.Sorting/python_sort_library.py)
- [Selection Sort](Algorithm/2.Sorting/selection_sort.py)
- [Insertion Sort](Algorithm/2.Sorting/insertion_sort.py)
- [Quick Sort](Algorithm/2.Sorting/quick_sort.py)
- [Counting Sort](Algorithm/2.Sorting/counting_sort.py)

### 3. Searching (탐색)

- [Binary Search](Algorithm/3.Searching/BinarySearch.py)

### 4. Dynamic Programming (동적 프로그래밍)

- [DynamicProgramming](Algorithm/4.Dynamic Programming/DynamicProgramming.py)

### 5. Shortest path (최단경로)

- [Dijkstra](Algorithm/5.ShortestPath/Dijkstra.py)
- [Floyd-Warshall](Algorithm/5.ShortestPath/Floyd-Warshall.py)

### 6. Graph Theory (그래프 이론)

- [DisjointSets](Algorithm/6.GraphTheory/DisjointSets.py)
- [Kruskal](Algorithm/6.GraphTheory/KruskalAlgorithm.py)
- [Topology](Algorithm/6.GraphTheory/Topology Algorithm.py)

### 7. Algorithm Theory (기타 알고리즘)

- [PartitionSum](Algorithm/7.AlgorithmTheory/PartitionSum.py)
- [PrimeNumber](Algorithm/7.AlgorithmTheory/PrimeNumber.py)
- [TwoPointer](Algorithm/7.AlgorithmTheory/TwoPointers.py)

### 8. Library (라이브러리) 

- [BasicLibrary](Algorithm/8.Library/BasicLibrary.py)
- [collections](Algorithm/8.Library/collections.py)
- [itertools](Algorithm/8.Library/itertools.py)
- [heapq](Algorithm/8.Library/heapq.py)
- [bisect](Algorithm/8.Library/bisect.py)


## Comments

### 1.  Greedy  (그리디)

 그리디 알고리즘은 주어진 상황에서 가장 최선의 선택을 하는 알고리즘이다. 장기적으로 보면 더 나은 결과를 도출할 수도 있겠지만 현재 가장 좋아보이는 판단을 한다. 구현이 가장 간단하다는 장점이 있다.

### 2. Realization (구현)

 구현 문제의 경우 떠올리는 아이디어는 쉽지만 그것을 코드로 만들기에 어려운 문제들을 구현 문제라고 한다.

### 3. DFS & BFS

 DFS는 깊이 우선탐색이라고 하고, BFS는 너비 우선 탐색이라고 한다.

- DFS: 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 인접행렬과 인접 리스트 방식이 존재한다. 데이터의 개수가 N개인 경우 $O(N)$의 시간이 소요된다.
- BFS: 가까운 노드부터 먼저 탐색하는 알고리즘이다. 큐 자료구조를 이용해서 구현한다.  `deque`라이브러리를 이용하고, O(N)의 시간이 소요된다.

### 4. Sorting (정렬)

정렬은 기본적으로 `sort()`와 `sorted()` 함수로 구현이 가능하긴 하다. 하지만 정렬의 기본이 되는 몇 가지 행렬의 알고리즘이 있다.

- 선택정렬
- 삽입정렬
- 계수정렬
- 퀵정렬
- 정렬 라이브러리

### 5. Searching (탐색)

 탐색 중에서 이진 탐색은 정렬된 상태에서만 사용이 가능한 탐색 방법이다. 순차 탐색보다 탐색시간이 O(log N)으로 줄어든다는 장점이 있다. 그래서 탐색의 범위가 매우 큰 데이터의 경우 이진 탐색으로 풀어야 하는 경우가 있다. 참고로 이진탐색을 하게해주는 라이브러리 `bisect`가 존재하기도 한다.

### 6. Dynamic Programming (동적 프로그래밍)

 다이나믹 프로그래밍은 이전의 연산을 다음 연산에 활용하게 될 경우 유용한 알고리즘이다. 가장 대표적인 예로 피보나치 수열을 들 수 있다. 점화식을 세울 수 있는 연산은 보통 Dynamic Programming으로 구현이 가능하다. 결과를 담은 리스트를 하나 생성해서 연산 기록을 남기는 방법이라고 할 수 있다.
 - 탑 다운 방식(메모이제이션 기법): 하향식 방법으로 재귀적으로 코드가 작성된다.
 - 바텀 업 방식: 상향식 방법으로 반복문을 사용한다. (권장하는 방법)

### 7. Shortest path (최단경로)
 최단경로 알고리즘은 보통 그래프를 이용해 표현하는데 각 지점은 '노드'(Vertex, Node)로 표현되고, 지점간 연결된 도로는 '간선'(Edge)로 표현된다. 다익스트라 알고리즘과 플로이드 워셜 알고리즘의 가장 큰 차이점은 1차원 배열을 생성하냐, 2차원 배열을 생성하냐이다. 다익스트라 알고리즘은 그리디 알고리즘인데 플로이드 워셜 알고리즘은 다이나믹 프로그래밍이라는 특징이 있다.

 - 다익스트라  알고리즘: **특정한 노드**에서 출발해 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘. 우선순위 큐인 `heapq`를 활용한 알고리즘 사용 시 O(ElogV)의 시간복잡도를 가진다.

 - 플로이드 워셜 알고리즘: **모든 지점**에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘. O(N^3) 시간복잡도를 가진다.


### 8. Graph Theory (그래프 이론)
 그래프 이론에는 여려가지가 있지만 그 중 '서로소 집합', '크루스칼 알고리즘', '위상정렬 알고리즘'이 자주 사용된다.

 - **서로소 집합**: 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조. union연산과 find연산으로 이루어져 있다. 노드의 개수가 V개이고, 최대 V-1개의 union연산과 M개의 find연산이 존재할 때 시간 복잡도는 대략 O(V+M(1+logV))
    - 무방향 그래프 내에서의 **사이클을 판별**할 때 사용(동일한 루트 노드를 가지는지 파악)

 - **크루스칼 알고리즘**: 신장트리(하나의 그래프의 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프)를 찾아야할 때 사용하는 알고리즘이다. 보통 최단경로를 찾는 '최소 신장 트리' 알고리즘을 많이 사용한다.  간선의 개수가 E일 때 시간 복잡도는 O(ElogE)이다.
    - 모든 도시를 연결하는 도로 연결 등에 사용


 - **위상정렬 알고리즘**: 순서가 정해져 있는 일련의 작업을 차례대로 수행해야할 때 사용하는 알고리즘. 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'. 진입차수(indegree)를 활용한다. 노드의 개수가 V, 간선의 개수가 E일 때시간 복잡도는 O(V+E)이다.
    - 과목 이수 순서 결정 등에 사용
- 
### 9. Algorithm Theory (기타 알고리즘)
위 알고리즘과는 별개로 코딩 테스트 문제에 자주 등장하는 기본 개념들이다.

- PartitonSum: 특정 리스트 구간의 합을 구하는데 사용한다. 여러 번 사용 될 만한 정보를 미리 구해서 저장해 놓는다. 결국 구간의 합은 P[R] - P[L-1]이 된다.

- TwoPointer: 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리한다. 부분합 문제나 두 개의 리스트를 합치는 문제에 사용한다.

- PrimeNumber: 소수 판별은 제곱근 방법과 에라토스테네스의 체 방법이 있다.
    - 제곱근 방법: 특정 자연수 N이 소수인지 판별할 때 사용하는 방법 sqrt(N)을 활용 해당 약수까지만 나누어 떨어지는 지 확인하면 된다.
    - 에라토스테네스의 체 방법: 특정 수 범위에서 소수의 개수를 확인할 때 사용하는 방법이다.
        - 2에서부터 시작해서 해당 수를 제외한 모든 배수를 제거해가면서 소수의 개수를 찾는다.

