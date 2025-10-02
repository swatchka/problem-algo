import sys
input = sys.stdin.readline

n = int(input())

cnt_price = 0
def best_coins(coins, target_price, idx = 0, cnt = 0):
    
    if target_price == 0: # 나머지가 0이면 지금까지 cnt 리턴 아니면 계속 진행
        return cnt
    
    if idx >= len(coins):
        return ('inf')   
    coin = coins[idx]
    
    use_cnt = target_price // coin # 쓸수 있는 동전의 갯수 카운트 
    if use_cnt > 0:
        cnt += use_cnt # 사용한 동전 카운트
        target_price %= coin # 나머지 체크
        
    return best_coins(coins, target_price, idx + 1, cnt) # 인덱스를 늘려주면서 다음 동전 사용
        
print(best_coins([5, 2], n))