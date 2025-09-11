#평균은 넘겠지
count = 0
case = int(input()) # 첫번째행 케이스 횟수
for i in range(case): 
    A = input().split()
    n = int(A[0])
    arr = A[1:1+n]
    arr = list(map(int, arr))
    avg = sum(arr) / n

    for x in arr:
        if x > avg:
            count += 1
    ratio = count / n * 100
    print(f"{ratio: .3f}%")
    