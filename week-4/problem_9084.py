import sys
input = sys.stdin.readline

t = int(input())
result_list = [0] * t

for o in range(t): # t번 실행
    n = int(input()) # 동전의 가지수 N
    coins = list(map(int, input().split()))
    amount = int(input())
    dp_list = [0] * (amount + 1) 
    dp_list[0] = 1 # 아무것도 선택하지 않을때

    for coin in coins: #ex) [1, 2, 3]
        for i in range(coin, amount + 1):
            dp_list[i] += dp_list[i-coin] # 모든 가능한 조합 누적
        result_list[o] = dp_list[amount]

for m in result_list:
    print(m)
