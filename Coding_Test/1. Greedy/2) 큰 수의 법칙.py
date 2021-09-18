## 큰 수의 법칙
# 리스트에서 큰 수를 출력하는 것

fir_line = "5 8 3"
sec_ilne = "2 4 5 4 6"

n, m, k = list(map(int,  fir_line.split(" ")))
sec_line = list(map(int, sec_ilne.split(" ")))

sec_line.sort(reverse=True)
max1 = sec_line[0]
max2 = sec_line[1]
result_sum = 0

# 풀이 1
####################

for x in range(1, m+1):
    if x % (k+1) == 0:
        result_sum += max2
        print(max2)
    else:
        result_sum += max1
        print(max1)
print(result_sum)


# 풀이 2
##################

count1 = (m/(k+1)*k + m % (k+1))
count2 = m/(k+1)
result = count1* max1 + count2 * max2

print(int(result))