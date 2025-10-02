import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dq = deque(range(1, n+1)) # 1부터 n까지의 숫자를 덱에 넣기
while len(dq) > 1: # 덱에 숫자가 하나 남을 때까지 반복
    dq.popleft() # 맨 앞의 숫자 제거
    dq.append(dq.popleft()) # 그 다음 숫자를 맨 뒤로 이동   

print(dq[0]) # 마지막으로 남은 숫자 출력
