import numpy as np
import sys
from collections import deque 
input = sys.stdin.readline

n, m = map(int, input().split()) # 새로 가로 입력
# my_array = np.full((n + 1, m + 1), 0)
arr_x = []
for _ in range(n):
    arr_x.append(input().strip())

arr = np.array([list(map(int, s.strip())) for s in arr_x], dtype=np.int8)
filled_arr = np.tile(arr, 1)

print(filled_arr.shape)
for row in filled_arr:
    print(row)
    
print(filled_arr.ndim)
#==================== 좌표평면 그리기 ==================== 

# target = filled_arr[n-1, m-1] # 목적지 좌표 추출
# print(target) 
def Breadth_First_Search(graph, start):
  # 이 줄이 빠지면 위처럼 한 방향만 저장됨
    queue = deque([start])
    visited = []
    visited = [start]

    
    while queue:
        curr_visited = queue.popleft()
        
        for next_node in graph.get(curr_visited, []):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
                
    return visited