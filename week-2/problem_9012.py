import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ps = input().strip()
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else: # p == ')'
            if stack:
                stack.pop()
            else:
                stack.append(p)
                break
    if stack:
        print("NO")
    else:
        print("YES")

