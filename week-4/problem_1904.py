import sys
input = sys.stdin.readline
n = int(input())

if n == 0: 
    print(0)    
    exit()

if n == 1:
    print(1)    
    exit()

if n == 2:
    print(2)    
    exit()

pibo = [0] * (n + 1)

pibo[1], pibo[2] = 1, 2 # 0은 이미 들어가 있기때문에 1번과 2번 인덱스만 1과 2로 고정
                        # pibo = [0, 1, 2, ~~]
for i in range(3, n+1): # i가 3부터 시작하기에 0, 1, 2를 따로 만들어 줘야한다.
    pibo[i] = (pibo[i-1] + pibo[i-2]) % 15746 # 피보나치 반복문 버전

print(pibo)
print(pibo[-1])