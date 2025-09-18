import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

dq = deque()
for _ in range(n):
    command = input().strip().split()
    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        if len(dq) == 0: # 예외처리 큐가 비어있을 때
            print(-1) 
        else:
            print(dq.popleft()) # 큐에서 첫번째 원소 제거
    elif command[0] == "size":
        print(len(dq)) # 큐의 크기 출력
    elif command[0] == "empty":
        if len(dq) == 0: # 큐가 비어있으면  
            print(1) # 1 출력
        else:
            print(0) # 아니면 0 출력
    elif command[0] == "front": # 큐의 첫번째 원소 출력
        if len(dq) == 0: # 예외처리 큐가 비어있을 때
            print(-1) # -1 출력
        else:
            print(dq[0]) # 큐의 첫번째 원소 출력
    elif command[0] == "back":
        if len(dq) == 0:
            print(-1) # 큐가 비었으면 -1 출력
        else:
            print(dq[-1]) # 큐의 마지막 원소 출력