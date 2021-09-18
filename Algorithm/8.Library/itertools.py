"""
# itertools
- 순열과 조합을 구현하는데 사용
- permutations, combinations
- product, combinations_with_replacement
    - product 연산은 permutations연산과 같지만, 원소를 중복해서 뽑는다.
    - combinations_with_replacement연산은 combinations연산과 같지만, 원소를 중복해서 뽑는다.
    - product연산은 사용법도 약간 다르다. 
- itertools로 생성된 변수는 itertools객체이기 때문에 list로 형변환 시켜줘야 한다.
"""

from itertools import permutations, combinations
# 순열
data = ["A", "B", "C"]
result = list(permutations(data, 2))
print(result)

# 조합
result2 = list(combinations(data, 2))
print(result2)

from itertools import product, combinations_with_replacement

# product
result3 = list(product(data, repeat=2))
print(result3)

# combinations_with_replacement
result4 = list(combinations_with_replacement(data, 2))
print(result4)