# 주어진 수가 1이 될 때까지의 연산

n, k = 25, 7
count = 0

while n>1:
    if n % k ==0: 
        n //= k
        count += 1
    else:
        n = n-1
        count += 1
print(count)