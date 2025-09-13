# 재귀함수 동전교환
def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    return count_change(amount,coins[1:]) + count_change(amount - coins[0], coins)