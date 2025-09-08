# 최댓값 2562
num = []
for _ in range(0, 9):
    num.append(int(input()))
for index, value in enumerate(num):
    dick = {value : index}
    full = max(num)
    if full == value:
        print(full)
        print(dick[value] + 1)
