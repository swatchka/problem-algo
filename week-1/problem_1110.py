s = input().strip().zfill(2)

index = list(s)
target = ''.join(index)
count = 0

print(target)
left = int(index[0])
right = int(index[1])

while True:
    left, right = right, (left + right) % 10
    count += 1
    curr = f'{left}{right}'
    if curr == target:
        break

print(count)