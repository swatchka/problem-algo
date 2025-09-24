import sys
sys.setrecursionlimit(10**6)

num = []
while True:
    try:
        s = input() 
    except EOFError:
        break
    if not s:        
        break
    num.append(int(s))

node = num

def postorder(start, end):
    if start > end:
        return
    root = node[start]
    mid = end + 1
    for i in range(start + 1, end + 1):
        if node[i] > root:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)

postorder(0, len(node) - 1)
