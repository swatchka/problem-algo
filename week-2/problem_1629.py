import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

def power(a, b, c): 
    if b == 0:  # b가 0일 때
        return 1 # 모든수의 0제곱은 1
    elif b % 2 == 0:   # b가 짝수일 때
        half = power(a, b // 2, c) # b를 반으로 나누어 재귀 호출
        return (half * half) % c # (a^(b/2) * a^(b/2)) % c
    else: # b가 홀수일 때
        return (a * power(a, b - 1, c)) % c # b에서 1을 빼서 짝수로 만들고 나중에 a를 한번 곱해줌
    
print(power(a, b, c))


