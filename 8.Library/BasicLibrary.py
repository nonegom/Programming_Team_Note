"""
# Math 라이브러리
- 팩토리얼, 제곱근, 최대공역수 등을 계산해주는 기능을 포함
"""
import math

# 팩토리얼(factorial)
print(math.factorial(5))

# 제곱근(sqrt): 제곱근은 결과값이 실수로 나온다.
print(int(math.sqrt(16)))

# 최대공약수(gcd)
print(math.gcd(10, 15))

# pi, e
print(math.pi, math.e)

"""
# 내장함수 
- import 없이 사용할 수 있는 함수
- sum(), min(), max(),sorted(), sort(), eval() 등의 함수가 있다.
"""
# sorted, sort
# sorted의 경우 리스트를 리턴한다. / sort의 경우 데이터 그 자체가 바뀐다.
data = [5, 3, 6, 2, 1]
data2 = sorted(data)
print(data, data2)
data.sort()
print(data)

# reverse=True를 통해 내림차순 전환이 가능
# key=lambda를 통해 정렬 순서를 정해줄 수도 있다.
name_list = [("가나다", 3), ("대머리", 7), ("홍길동", 5)]
data3 = sorted(name_list, key=lambda x: x[1], reverse = True)
print(data3)

"""
List Comprehension, Lambda Function, Map, Filter
"""

# 리스트 컴프리핸션
x = [i for i in range(10)]
y = [i for i in range(10) if i%2==0] # 짝수만 출력
print(x, y)

# 람다함수
even = (lambda x : True if x % 2 ==0 else False)

# map & fliter 
# map은 iteration 객체의 값 모두가 변하지만, filter의 경우 조건에 맞는 값만 출력한다.

# map: iteration 객체에 함수를 적용시킨 값을 출력
print(list(map(lambda x: "짝수" if x%2 ==0 else "홀수", x)))

# filter: iteration객체에 함수를 돌려 함수에 조건에 맞는 값만 출력하는 메소드 (map과는 다르게 )
print(x)
print(list(filter(even, x))) 


