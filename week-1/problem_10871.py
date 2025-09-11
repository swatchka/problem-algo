# X보다 작은수 10871
N, X = map(int, input().split()) # X는 비교할 숫자, N이 리스트의 길이, A가 리스트
A = [0] * N
A = list(map(int, input().split()))
for i in range(0, N):
    if X > A[i]:
        print(A[i], end=" ")