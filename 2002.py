from collections import deque

cnt = 0 # 추월한 차량의 개수

N = int(input())
q = deque()

# 터널 들어가는 차량 입력
for i in range(N):
    q.append(input())
    
# 터널 나오는 차량을 입력받고 처리
for i in range(N):
    out = input()
    
    # 추월한 차량
    # 추월한 차량을 처리한 후 제거해주어야 함 그래야 작업이 원활하게 진행됨
    if out != q[0]:
        q.remove(out)
        cnt += 1
        
    else:
        q.popleft()
        
print(cnt)
    