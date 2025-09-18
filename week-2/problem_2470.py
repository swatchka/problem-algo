# n = int(input())
# liquid = list(map(int, input().split()))
# sorted_liquid = sorted(liquid)

# print(sorted_liquid)
# def binary_search(arr):
#     target_pair = min(
#         ((x, y) for i, x in enumerate(arr) for y in arr[i+1:]),
#         key=lambda pair: (abs(pair[0] + pair[1]), pair[0] + pair[1] < 0)
#     )
#     return f"{target_pair[0]} {target_pair[1]}"
# def binary_search(arr, target = []): # 이분탐색
#     left, right = 0, len(arr) - 1 
#     target_pair = min(
#     ((x, y) for i, x in enumerate(sorted_liquid) for y in sorted_liquid[i+1:]),
#     key=lambda pair: (abs(pair[0] + pair[1]), pair[0] + pair[1] < 0)
#     )
#     tar_list = []
#     for i in liquid:
#         if i in target_pair:
#             tar_list.append(i)
#             target_pair = tuple(x for x in target_pair if x != i)
#         if len(tar_list) == 2:
#             break 
#     target = sum(tar_list)
#     while left < right: # 타겟값과 같은 수가 나올때까지 이진탐색 조지는 반복문
#         mid = (left + right) // 2 # 중간값 계산
#         if arr[mid] == target: 
#             print(mid)
#             return f"{arr[left]} {arr[right]}"
#         elif arr[mid] < target: # 오른쪽으로 탐색
#             left = mid + 1
#         else: # arr[mid] > target // 왼쪽으로 탐색
#             right = mid - 1
    
#     return "예외 발생"  # 예외처리 (-1 반환)

# print(binary_search(sorted_liquid))

import sys
# input = sys.stdin.readline
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left, right = 0, n - 1
best_sum = float('inf')
best_a, best_b = arr[left], arr[right]

while left < right:
    s = arr[left] + arr[right]

    # 더 좋은 쌍이면 갱신 (동점일 때는 사전순으로 작은 쌍 선택 → 출력 일관성)
    if abs(s) < abs(best_sum) or (abs(s) == abs(best_sum) and (arr[left], arr[right]) < (best_a, best_b)):
        best_sum = s
        best_a, best_b = arr[left], arr[right]

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        # 합이 정확히 0이면 최적
        best_a, best_b = arr[left], arr[right]
        break

# 오름차순으로, 괄호 없이 출력
print(best_a, best_b)