import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0
def divide_and_conquer(x, y, n):
    global white, blue  # 전역변수 사용
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                divide_and_conquer(x, y, n // 2) # 1사분면
                divide_and_conquer(x, y + n // 2, n // 2) # 2사분면
                divide_and_conquer(x + n // 2, y, n // 2) # 3사분면
                divide_and_conquer(x + n // 2, y + n // 2, n // 2) # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return
divide_and_conquer(0, 0, n)
print(white)
print(blue)


