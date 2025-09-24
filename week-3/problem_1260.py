# DFS 깊이 우선탐색
# BFS 너비 우선 탐색
# 을 각각 출력하는 프로그램
import sys
input = sys.stdin.readline
from collections import deque 
n, m, v = map(int, input().split()) # n = 노드의 갯수, m = 엣지의 갯수, v = 시작 루트

node = {}

for i in range(1, n+1):
    node[i] = []
    
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    
for key in node:
    node[key].sort()

def Depth_First_Search(graph, start, visited = []):

    visited.append(start) # 현재 노드 방문 표시
    
    for node in graph.get(start, []): # 자식 노드 순회
        
        if start not in visited:
            visited.append(start)
            
        if node not in visited: # 중복 방지
            Depth_First_Search(graph, node, visited) # 재귀 호출
            
    return visited         

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
            
dfs = Depth_First_Search(node, v)
bfs = Breadth_First_Search(node, v)

print(*dfs)
print(*bfs)

