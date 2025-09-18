import sys
input = sys.stdin.readline

n = int(input()) # 막대기 수
heights = [int(input()) for _ in range(n)] # 높이 입력 받기
max_height = 0 # 현재까지 가장 높은 막대기
count = 0 # 보이는 막대기 수

for height in reversed(heights): # 뒤에서부터 확인
    if height > max_height: # 현재 막대기가 지금까지 가장 높은 막대기보다 높으면
        count += 1 # 보이는 막대기 수 증가
        max_height = height # 가장 높은 막대기 갱신

print(count) # 결과 출력
