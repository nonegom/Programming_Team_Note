"""
# Collections
- 코딩테스트에서 자주 사용하는 deque와 counter가 있는 라이브러리

### deque
- 큐나 스택을 구현하는데 사용하는 메소드
- append(), pop(), appendleft(), popleft()

### Counter (카운터는 객체가 대문자)
-등장 횟수를 세는 기능을 제공
- List와 같은 iterable 객체가 주어졌을 때 해당 객체 내부의 원소가 몇 번씩 등장하는지를 알려준다.
- 코딩 테스트에서 개수를 셀 때 굉장히 유용하게 사용된다.
"""

# deque
from collections import deque
data = deque([2, 3, 4])
data.append(5)
data.appendleft(1)

print(data)

# counter
from collections import Counter
data2 = ["blue", "yellow", "red", "red", "yellow", "blue", "blue"]
counter = Counter(data2)
print(counter["blue"])
dict(counter)