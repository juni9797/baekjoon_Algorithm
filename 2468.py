# 안전영역
# 인접한 영역은 1개의 영역으로 취급한다
# 대각선으로만 연결된 부분은 연결이 아니라고 생각한다
# 어디까지 물에 잠겼다고 해야 물에 잠기지 않은 최대 영역의 갯수를 구할 수 있는가?
# 가령 5까지 물이 잠겼다고 하면 물에 잠기지 않은 영역의 갯수는 5개임 --> 이게 최대 갯수가 되는 것
# 3까지 물에 잠겼다고 하면 물에 잠기지 않은 영역의 갯수는 4임
# 여기서 중요한 부분은 연결되어 있는 부분을 1개로 치는 것
# 연결되어 있는 개념 또는 노드의 개념을 풀 때는 bfs/dfs 생각하자 --> 연결되어 있는 개념이 등장하는 문제는 bfs/dfs 둘 다 적용해도 풀림

# 만일 2보다 높은 숫자라고 한다면 동서남북으로 4가지 방향을 전부 탐색하게 되는것
# 여기서 2보다 작은 수라면 지우고 높은 숫자로만 뻗어 가는 것
# 다만 내가 온 경로는 세지 않음, 2-8로 갔다면, 8에서 4방향으로 뻗어갈 때 내가 온 2는 제거하는 것

# 코드를 한번에 짤 생각보다 코드 보고 이해하는 것을 우선으로 삼자
# 이거 꽤 어려움

from collections import deque
 
n = int(input()) # 입력 받기
max_num = 0
graph = []
 
for _ in range(n):
    
    # 한줄 씩 입력받아서 
    low = list(map(int, input().split()))  # N * N 배열
    graph.append(low)
 
    # 한줄에서 최댓값을 찾고, 그전까지의 최댓값과 비교해서, 전체에서 제일 높은 지대 찾기.
    for i in low:
        if i > max_num:
            max_num = i # 최댓값을 찾는다. 제일 높은 지대.

# 동서남북 방향을 배열에 넣고,
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
 
# 안전지대 숫자가 num
def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
 
    while queue:
        x, y = queue.popleft()
 
        # 연결 되있는 지점 찾기. 총 4가지 방향 검사
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
 
            if 0 <= nx < n and 0 <= ny < n:
                # 즉, 안전지대라면, 방문처리를 한다. 0이면 방문이 아직 안된것들
                if graph[nx][ny] > num and visited[nx][ny] == 0:
                    # 방문처리
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
 
result = []

for i in range(max_num):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            
            # 안전지대 개수를 세어줌.
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
                
    # 각각의 높이에 대해서 안전지대 영역의 개수를 result 저장
    result.append(cnt)

# 안전지대의 최대값은 result max가 됌
print(max(result))