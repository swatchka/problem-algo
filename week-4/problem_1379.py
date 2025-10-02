import sys
input = sys.stdin.readline
import heapq

k = int(input())
#우선 순위 큐 저장 배열선언
heap =[]

answer= [0] * (k+1)
lecture = [list(map(int,input().split())) for _ in range(k)]

lecture.sort(key=lambda x:(x[1],x[2]))

#1은 강의실번호 
room_num=1
heapq.heappush(heap,[lecture[0][2],room_num])
answer[lecture[0][0]] = room_num


for i in range(1,k):
    if heap[0][0] > lecture[i][1]:
        room_num +=1   
        answer[lecture[i][0]] = room_num
        heapq.heappush(heap,[lecture[i][2] ,room_num])

    else:
        temp = heapq.heappop(heap)
        answer[lecture[i][0]] = temp[1]
        heapq.heappush(heap,[lecture[i][2],temp[1]])


print(len(heap))
for i in range(1,len(answer)):
    print(answer[i])

