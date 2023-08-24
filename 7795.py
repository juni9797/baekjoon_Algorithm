# 시간 복잡도는 n*m임
# 왜? 문제 페이지 그림을 보면 왼쪽 8(n에 해당) 오른쪽의 3,6,1(m에 해당)과 수를 비교하는 것이기 때문에 시간 복잡도를 가늠할 수 있음
# 그래서 시간초과가 걸릴 가능성이 있음
# 나보다 작은 물고기들이 몇 개 존재하는지 전부 확인하지 않고 파악하려면 m을 크기순으로 정렬해서 가장 큰 수와  n을 비교한다면
# 만일 m의 가장 큰 수보다 n보다 작다면 m의 모든 수가 n보다 작다는 결론이 나오기 때문에 일일이 계산 안하고 결론을 얻을 수 있음
# 이건 내 추측인데 강사님 솔루션은 정렬 후 이진탐색 활용하라는 것
# n과 가장 가까운 m을 잡고(중간값) 탐색을 진행하는 것
# 만일 여기서 n=8, m = 1,3,6,10,20이면 중간값 6을 찯고 6의 인덱스 값의 +1을 해주면(2+1) 내가 먹을 수 있는 물고기의 갯수가 나오는 것

def binary_search(fish_list, eat_fish):
    
    s = 0
    e = len(fish_list) - 1
    result = -1
    while s <= e:

        m = (s + e)//2
        
        if fish_list[m] < eat_fish:
            result = m
            s = m + 1
        else:
            e = m - 1

    return result



T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for j in A:
        cnt += (binary_search(B, j) + 1) # j 물고기가 먹을 수 있는 총 물고기 개수
    print(cnt)