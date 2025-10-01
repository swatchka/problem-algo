# # n = 회의실 갯수
# # 회의 시간이 가장 짧은것 먼저 베정
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# cabinet = []
# n = int(input())
# for _ in range(n):
#     start, end = map(int, input().strip().split())
#     cabinet.append([start, end])

# def end_time(cabinet):
#     return cabinet[1]

# cabinet.sort(key=end_time)

# cnt_meeting = 0
# end_time = 0

# def max_meetings(cabinet, last_end=0, idx=0):
    
#     if idx >= len(cabinet): # 인덱스 카운트
#         return []

#     start, end = cabinet[idx]

#     if start >= last_end:
#         return [(start, end)] + max_meetings(cabinet, end, idx + 1)
#     else:
#         return max_meetings(cabinet, last_end, idx + 1)
    
# print(len(max_meetings(cabinet)))

import sys
input = sys.stdin.readline

cabinet = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().strip().split())
    cabinet.append((start, end))

cabinet.sort(key = lambda x: (x[1], x[0]))

cnt_meeting = 0
end_time = 0

for meeting_times in cabinet:
    if meeting_times[0] >= end_time:
        cnt_meeting += 1
        end_time = meeting_times[1]

print(cnt_meeting)


