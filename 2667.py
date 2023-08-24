# 단지 번호 붙이기
# dfs/bfs 이용


from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1 , 0, 0]

def bfs(arr, i, j):
    
    N = len(arr) # 가로의 길이
    queue = deque()

    # i, j 좌표에 대한 방문처리
    queue.append((i, j))
    arr[i][j] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0  # 방문처리 (배열에서 단지계산을 하지 않고, bfs안에서도 연결된 노드로 계산하지 않는다)
                queue.append((nx, ny))
                count += 1

    return count  # 집의 숫자
                


# 입력
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
    
cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt.append(bfs(arr, i, j)) # bfs로 단지에 있는 총 연결된 1의 개수

print(len(cnt)) # 단지의 개수
cnt.sort()
for i in cnt:
    print(i)

