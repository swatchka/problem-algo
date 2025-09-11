x, y = map(int,input().split())
t = int(input())
X, Y = [0], [0]
for _ in range(t):
    angle, num = map(int,input().split())
    if angle == 1:
        Y.append(num)
    else:
        X.append(num)
X.append(y)
Y.append(x)
X = sorted(X)
Y =  sorted(Y)
max_lenX = []
max_lenY = []
for i in range(-1, -len(X), -1):
    max_lenX.append(X[i] - X[i-1])
for j in range(-1, -len(Y), -1):
    max_lenY.append(Y[j] - Y[j-1])
max_x = max(max_lenX)
max_y = max(max_lenY)
print(max_x * max_y)



