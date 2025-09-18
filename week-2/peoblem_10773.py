import sys
input = sys.stdin.readline
k = int(input()) # 입렵 횟수
stack = []
total = 0

for _ in range(k): 
    num = int(input().strip())
    if num == 0: 
        if stack:
            total -= stack.pop()
            
    else:
        stack.append(num)
        total += num

print(total)