
# 수 찾기(이분탐색)

# 이분탐색의 기본 구조
# 1. 입력받기 - 2개의 리스트 중 비교 대상이 되는 리스트는 정렬을 해야 함
# 2. for문 구성 - for문에서 핵심은 start, end, 숫자 존재 여부를 구분해주는 변수를 False로 넣는 것
    #  왜? 이후 나오는 while문에 이것들을 넣게 되면 if문의 결과에 따라 start, end값이 바뀌게 되는데
    # 그러면 바뀐 값으로 이분탐색이 되는 것이 아니라 원치 않는 기본값으로 설정되기 때문
# 3. while문 구성 - 핵심은 start가 end보다 크거나 같을 때 반복을 중단한다는 것
    # while문 안에 mid값을 설정 왜? mid값은 if문 결과에 따라 start와 end값이 계속 바뀌고
    # 이를 반영하여 mid값을 설정해야 하기 때문
# 4. if문 구성 - 핵심은 i와 n_list[mid]를 비교
    # i와 n_list[mid]가 같다면, 해당 리스트에 일치하는 수가 있기 때문에 프린트를 하고, true값으로 바꾸고 반복문을 빠져 나와야 함
# 5. 반복문을 끝까지 돌렸음에도 일치하는 수가 안나왔을 경우 - 0을 출력한다 : 핵심은 이 코드 또한 맨 처음 for문 안에 있어야 함

# 코드를 전체적으로 간략하게 보면
# 입력부분 + for문(while(if()), False일 경우)


n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    # for문 안에서 start, end을 정의
    # 추가로 일치하는 수를 찾았을 경우 True, 아닌 경우 False로 정의
    # 기본값은 False임 왜? 찾았을 경우 트루고 못찾으면 변동없이 지나다가 false를 출력해야 하기 때문
    start = 0
    end = n-1
    find = False
    
    # 이제 반복문에 들어가는데 for가 아닌 while을 씀
    # start가 end보다 커지게 되면 반복문을 탈출하게 되는 것
    while start <= end:
        # 여기서 mid를 정의함 왜? mid는 반복문이 돌아갈 때마다 계속 바뀌고 초기화 되야 하기 때문
        # mid는 start와 end의 중간값을 취함
        mid = (start+end)//2
        
        # 여기서부터 if문으로 n_list[mid]와 i값을 비교
        if i == n_list[mid]:
            # 만일 m_list안의 i값이 n_list[mid]와 같다면
            # 해당 수가 n_list가 존재한다는 표시로 find = True로 잡아줌
            # 그리고 문제에서 원하는 바대로 1을 프린트하고
            # 바로 반복문에서 탈출(해당 수가 존재하는지 여부가 중요하기 때문에 반복문을 더 돌릴 이유가 없음)
            find = True
            print(1)
            break
        
        # i값이 mid값보다 큰 경우
        # mid +1을 하고 그 값을 start로 잡음 왜? 여기 elif문까지 넘어왔다는 것은 i값이 n_list[mid]값과 다르다는 것
        # 따라서 n_list[mid+1 = start] 이렇게 잡고, 미드값을 다시 잡은 다음 이분탐색 다시 진행하는 것
        elif i > n_list[mid]:
            start = mid + 1

        # i가 n_list[mid]보다 작은 경우도 마찬가지
        else:
            end = mid-1
        
    if find == False:
        print(0)
        
