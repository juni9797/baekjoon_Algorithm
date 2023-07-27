
# 2798 블랙잭

n, m = map(int, input().split(" "))

card_list = list(map(int, input().split(" ")))

result = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum > m:
                continue
            else:
                result.append(sum)
                
print(max(result))

