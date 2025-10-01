# top-down 방식 (메모리제이션)

n = int(input())
memo = [0 for _ in range(n+2)] 
memo[1], memo[2] = 1, 1
def pibo(n):
    if memo[n] == 0:
        memo[n] = pibo(n-1) + pibo(n-2)

    return memo[n]

print(pibo(n))
print(memo)
