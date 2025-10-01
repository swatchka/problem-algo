# 물건을 선택하지 않을떄

N, K = map(int, input().split())
Backpack = []
Backpack.append(0)
for i in range(N):
    Backpack.append(tuple(map(int, input().split())))
#print(Backpack)
DP = []
for i in range(K + 1):
    row = []
    for j in range(N + 1):
        row.append(0)
    DP.append(row)
#print(DP)
worth = 0
for i in range(1, K+1):
     for j in range(1, N+1):
        if i >= Backpack[j][0]:
            DP[i][j] = max(DP[i][j-1], DP[i - Backpack[j][0]][j-1] + Backpack[j][1])
        else:
            DP[i][j] = DP[i][j-1]
print(DP[K][N])