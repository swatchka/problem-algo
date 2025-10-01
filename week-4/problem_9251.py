# 알파뱃 배열을 다루는 두 수열의 공통으로 연속된 부분
# 대문자 A부터 Z까지 아스키 코드(65 ~ 90) X 답 없음
# 같은것 끼리 검사하며 연속 체크

import sys
input = sys.stdin.readline

str2 = list(input().strip())
str1 = list(input().strip())

dp_list = []
for _ in range(len(str2) + 1):
    row = [0] * (len(str1) + 1)
    dp_list.append(row)

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            dp_list[i][j] = dp_list[i-1][j-1] + 1
        else:
            dp_list[i][j] = max(dp_list[i-1][j], dp_list[i][j-1])
           
print(max(max(dp_list)))
# print(dp_list)
# for row in dp_list:  # 각 행(안쪽 리스트)을 순회
#     for element in row:  # 각 행의 요소들을 순회
#         print(element, end=" ") # 요소를 출력하고 한 칸 띄어쓰기
#     print() # 한 행의 출력이 끝나면 줄바꿈