# 그리디 알고리즘
# 동전 0
# 실버 4

n,k = map(int, input().split(" "))

list = []

for i in range(n):
    a = int(input())
    list.append(a)

list.reverse()

count = 0

for i in list:
    count = count + (k // i)
    k = k % i
    
print(count)