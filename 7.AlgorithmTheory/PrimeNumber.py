# 소수 판별
## 소수 판별은 크게 제곱근 방법과 에라토스테네스의 체 방법으로 해결가능하다고 할 수 있겠다.

## 제곱근 방법
### 특정 자연수 N이 소수인지 판별할 때 사용하는 방법 [제곱근 math.sqrt(n) 까지만 계산]

## 에라토스테네스의 체 방법
### 특정 수 범위에서 소수의 개수를 확인할 때 사용하는 방법이다.

import math
def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 :
            return print("소수가 아닙니다")
    return print("소수입니다.")

is_prime_number(23)


## 에라토스테네스의 체

import math

def eratosthenes(n):
    tmp = [True]*(n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if tmp[i] == True:
            j = 2
            while (i*j) <= n:
                tmp[i*j] = False
                j += 1
    tmp[0], tmp[1] = False, False
    for i, v in enumerate(tmp):
        if v:
            print(i, end = " ")
eratosthenes(100)