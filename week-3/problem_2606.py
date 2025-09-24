import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

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

    for node in graph.get(start, []): # 자식 노드 순회
        
        if start not in visited:
            visited.append(start)
            
        if node not in visited: # 중복 방지
            Depth_First_Search(graph, node, visited) # 재귀 호출
            
    return visited 

dfs = Depth_First_Search(node, 1)
if (len(dfs) - 1) < 0:
    print(0)
else:
    print(len(dfs) - 1)