# 직사각형에서 탈출 1085
x, y, w, h = map(int, input().split())
a = x - w
b = y - h
c = x - 0
d = y - 0
print(min(abs(a), abs(b), abs(c), abs(d)))