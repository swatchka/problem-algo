import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dq = deque(range(1, n+1)) # 1부터 n까지의 숫자를 덱에 넣기
result = [] # 제거된 순서를 저장할 리스트

while dq: # 덱이 빌 때까지 반복
    dq.rotate(-k+1) # 큐를 통째로 -k+1칸 밈
    result.append(dq.popleft()) # 맨 앞의 숫자 제거 후 결과 리스트에 추가   
    
print("<" + ", ".join(map(str, result)) + ">") # 양 옆에 꺽쇠 붙여서 출력

# =========================== 다른 풀이 ===========================
# 시프트 연산 
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())
# dq = deque(range(1, n+1))

# while dq:
#     for _ in range(k-1):      # k-1번 앞으로 밀어서 원하는 숫자가 맨 앞으로 오게 유도
#         dq.append(dq.popleft())
#     print(dq.popleft())   # k번째 제거와 동시에 출력