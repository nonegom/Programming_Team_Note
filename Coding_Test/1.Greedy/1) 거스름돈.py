# 거스름돈
# 입력이 들어왔을 때 각 돈에 해당하는 잔돈을 반환

n = 1260 
count = 0
coin_types = [500, 100, 50, 10]

for i in coin_types:
    count += n // i
    n = n % i
print("코인의 개수: ", count)

def change(x):
    ls_res = [0 for _ in range(4)]
    while x > 10:
        if x >= 500: 
            ls_res[0] = x//500
            x = x % 500
        elif x >= 100: 
            ls_res[1] = x // 100
            x = x % 100
        elif x >= 50: 
            ls_res[2] = x // 50
            x = x % 50
        else:
            ls_res[3] = x//10
            x = x%10
    return ls_res