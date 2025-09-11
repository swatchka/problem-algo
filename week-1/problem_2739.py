# 구구단 2739
N = int(input())
for i in range(1, 9):
    print("""{N} * {i} = {result}""".format(N = N, i = i, result = N * i))