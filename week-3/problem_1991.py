# 노드 7개
# 엣지는 (7-1) = 6개
# 입력값 맨 위 정수는 노드의 개수
# 루트 노드는 항상 A
# 자식 노드가 없으면 .으로 표현
# 첫번째 세로줄 : 부모 노드
# 두번째 세로줄 : 왼쪽 자식 노드
# 세번째 세로줄 : 오른쪽 자식 노드
import sys
input = sys.stdin.readline
n = int(input())
tree = {} # 딕1셔너리로 트리 표현

for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = (left, right) # (왼쪽 자식, 오른쪽 자식)
    
    def preorder(node): # 전위 순회
        if node == '.': 
            return # 종료
        print(node, end='') # 루1트먼저
        preorder(tree[node][0]) # 왼쪽 자식 방문
        preorder(tree[node][1]) # 오른쪽 자식 방문
        
    def inorder(node): # 중위 순회
        if node == '.': 
            return # 종료
        inorder(tree[node][0]) # 왼쪽 자식 방문
        print(node, end='') # 왼쪽 자식이 더이상 없을때 출력
        inorder(tree[node][1]) # 오른쪽 자식 방문
        
    def postorder(node): # 후위 순회
        if node == '.': 
            return # 종료
        postorder(tree[node][0]) # 왼쪽 자식 방문
        postorder(tree[node][1]) # 오른쪽 자식 방문
        print(node, end='') # 오1른쪽 자식이 더이상 없을때 출력
        
print(tree)
preorder('A') # 루트 노드부터 시작
print() # 줄바꿈

inorder('A') 
print() 

postorder('A')
print()
