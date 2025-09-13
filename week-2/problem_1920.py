# 첫째 줄에 자연수 N
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_set = set(n_list)
m_set = set(m_list)

# print(n_set)
# print(m_set)
for x in m_list:
    if x in n_set:  
        print(1)
    else:
        print(0)
