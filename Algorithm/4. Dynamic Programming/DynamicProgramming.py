# 피보나치 수열 예제

# Top-Down (재귀)
x = 100
df = [0]*(x+1)
def pibo(n):
    if n == 1 or n == 2:
        return 1
    if df[n]!= 0:
        return df[n]
    df[n] = pibo(n-1) + pibo(n-2)
    return df[n]
pibo[10]

# Bottom-Up (반복)
n = 100
df = [0]*n+1
df[1], df[2] = 1, 1
for i in range(3, n+1):
    df[i] = df[i-1]+df[i-2]
df[10]

## 리스트는 보통 0부터 시작하게 된다. 그래서 1~100까지 등 자연수에 일일이 대응시키기 위해서는 약간의 꼼수가 필요하다.
## 위에서 처럼 [0]째 리스트를 비우고, n+1의 길이의 리스트를 만들어주면 바로 원하는 번호에 접근이 가능하다.