# OX 퀴즈
case = int(input()) # 사이클 입력받기

for i in range(case): # 그 사이클 만큼 입력받을 반복문
    ans = list(input()) # 입력받은 값을 리스트에 저장 ['o', 'x', 'o', 'o']
    score = 0 # 점수 변수 선언
    plus_score = 0 # 연속되는 o의 추가점수를 카운트할 변수 선언
    for i in ans: # 입력된 값에 있는 o와 x를 판별한 반복문
        if i == 'O': # o문자 판별
            plus_score += 1 # 반복되는 o의 갯수에 따라 추가점수 가산
            score = score + plus_score # 추가점수 합산
        elif i == 'X': # x판별
            plus_score = 0  # x가 있을때 추가점수 초기화
    print(score)