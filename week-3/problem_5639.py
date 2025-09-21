num = []
while True:
    num.append(input())
    if num[-1] == "":
        num.pop()
        node = list(map(int, num))
        break
   
    if num[-1] == "EOF":
        num.pop()
        node = list(map(int, num))
        break
    if num[-1] == " ":
        num.pop()
        node = list(map(int, num))
        break
    if num[-1] == "\n":
        num.pop()
        node = list(map(int, num))
        break
    if num[-1] == "\r\n":
        num.pop()
        node = list(map(int, num))
        break
    
def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if node[start] < node[i]:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(node[start])
postorder(0, len(node) - 1)

    
