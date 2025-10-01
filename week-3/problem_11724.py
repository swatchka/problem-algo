import sys
input = sys.stdin.readline
from collections import deque 

n, m = map(int, input().split())

node = {}

for i in range(1, n+1):
    node[i] = []
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for key in node:
    node[key].sort()
# print(node)

def Depth_First_Search(graph, s, visited):
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            Depth_First_Search(node, i, visited)
    return visited      
cnt = 0 # 연결 노드의 수
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        Depth_First_Search(node, i, visited)
        cnt += 1
print(cnt)