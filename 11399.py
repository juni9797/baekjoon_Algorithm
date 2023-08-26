# atm 아틀레티코마드리드
# 

n = int(input())

time_list = list(map(int,input().split(" ")))

time_list.sort()

time = 0
min_time = 0

for i in time_list:
    time = time + i
    min_time = min_time + time
    
    
print(min_time)
ß