# 수 찾기

n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))


for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)


# 어떤 값을 탐색할 때 리스트로 탐색하게 되면 시간 복잡도가 O(n)이다
# 즉, 1-10,000,000 값을 탐색할 때 리스트는 맨 마지막 값을 검사할 때는 처음부터 끝까지 10,000,000번을 탐색하게 되는 것
# 근데 여기서 set이나 dict를 쓰면 시간 복잡도를 O(1)로 단축할 수 있다
# 따라서 문제와 같이 데이터를 in으로 검색하고자 할 떄는 set으로 받아서 탐색하면 빠르게 탐색할 수 있다.