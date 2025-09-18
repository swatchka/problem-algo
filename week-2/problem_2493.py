import sys
input = sys.stdin.readline 
n = int(input()) # 막대기 수

heights = list(map(int, input().split()))  # 막대기 높이 리스트
stack = [] # (인덱스, 높이) 형태로 저장
result = [0] * n # 결과를 저장할 리스트, 기본값은 0

for i in range(n): # 탑 갯수만큼 반복과 동시에 인덱스 카운팅
    while stack: # 스택이 비어있지 않으면
        if stack[-1][1] > heights[i]: # 스택의 맨위 탑의 높이가 현재 높이보다 크면
            result[i] = stack[-1][0] + 1 # 그 탑을 수신자로 인식, 인덱스 저장
            break # 반복문 종료
        stack.pop() # 스택의 마지막 높이가 현재 높이보다 작으면 스택에서 제거
    stack.append((i, heights[i])) # 현재 인덱스와 높이를 스택에 추가
    
    
print(" ".join(map(str, result))) # 결과 출력
