from __future__ import annotations
# 이진 검색 트리
from typing import Any, Optional

class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        
        self.key = key # 키
        self.value = value # 값
        self.left = left # 왼쪽 포인터
        self.right = right # 오른쪽 포인터
        
class BinarySearchTree:
    
    def __init__(self):
        self.foot = None
        
    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
        
    def add(self, key: Any, value: Any) -> bool:
        
        def add_node(node: Node, key: Any, value: Any) -> None:
            
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        
    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True
        
        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                    
                else:
                    is_left_child = False
                    p = p.right
                    
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.left = p.right
        
        elif p.right is None:
            if p.right is None:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
            
        return True
    
    def dump(self) -> None:
        def print_subtree(node: Node) -> None:
            if node is not None:
                print_subtree(node.left)
                print(f"{node.key} {node.value}")
                print_subtree(node.right)
                
        print_subtree(self.root)
        
    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key
    
    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
    
    def dump(self, reverse = False) -> None:
        def print_subtree(node: Node) -> None:
            if node is not None:
                if reverse:
                    print_subtree(node.right)
                    print(f"{node.key} {node.value}")
                    print_subtree(node.left)
                else:
                    print_subtree(node.left)
                    print(f"{node.key} {node.value}")
                    print_subtree(node.right)
                    
        print_subtree(self.root)
        
        def print_subtree(node: Node, level: int) -> None:
            if node is not None:
                print_subtree(node.right, level + 1)
                print(" " * 4 * level + "->", node.key)
                print_subtree(node.left, level + 1)
        print_subtree(self.root, 0)
    def height(self) -> int:
        def height_subtree(node: Node) -> int:
            if node is None:
                return 0
            h_left = height_subtree(node.left)
            h_right = height_subtree(node.right)
            return max(h_left, h_right) + 1
        return height_subtree(self.root)
    def count(self) -> int:
        def count_subtree(node: Node) -> int:
            if node is None:
                return 0
            return count_subtree(node.left) + count_subtree(node.right) + 1
        return count_subtree(self.root)
    def clear(self) -> None:
        self.root = None
    root: Optional[Node] = None
if __name__ == "__main__":
    btree = BinarySearchTree()
    while True:
        menu = input("삽입(I)/삭제(D)/검색(S)/덤프(P)/최소(M)/최대(X)/높이(H)/개수(C)/초기화(Z)/종료(Q): ").upper()
        if menu == "I":
            key = int(input("키를 입력하세요.: "))
            val = input("값을 입력하세요.: ")
            if btree.add(key, val):
                print(f"{key} {val} 삽입됨.")
            else:
                print(f"{key} 이미 존재함.")
        elif menu == "D":
            key = int(input("삭제할 키를 입력하세요.: "))
            if btree.remove(key):
                print(f"{key} 삭제됨.")
            else:
                print(f"{key} 없음.")
        elif menu == "S":
            key = int(input("검색할 키를 입력하세요.: "))
            val = btree.search(key)
            if val is not None:
                print(f"{key}의 값은 {val}입니다.")
            else:
                print(f"{key} 없음.")
        elif menu == "P":
            btree.dump()
        elif menu == "M":
            key = btree.min_key()
            if key is not None:
                print(f"최소 키는 {key}입니다.")
            else:
                print("트리가 비어있습니다.")
        elif menu == "X":
            key = btree.max_key()
            if key is not None:
                print(f"최대 키는 {key}입니다.")
            else:
                print("트리가 비어있습니다.")
        elif menu == "H":
            h = btree.height()
            print(f"트리의 높이는 {h}입니다.")
        elif menu == "C":
            c = btree.count()
            print(f"노드의 개수는 {c}입니다.")
        elif menu == "Z":
            btree.clear()
            print("트리를 초기화했습니다.")
        elif menu == "Q":
            break
        else:
            print("메뉴를 잘못 입력했습니다. 다시 입력하세요.")
# 이진 검색 트리
