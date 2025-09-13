N, M = map(int, input().split()) # N은 나무갯수, M은 필요한 나무 길이
Tree_list = list(map(int, input().split()))

Sorted_Tree_List = sorted(Tree_list)

def cut_trees(Sorted_Tree_List, M, start, end, result=0):
    if start > end:
        return result
    
    mid = (start + end) // 2
    total = 0
    for tree in Sorted_Tree_List:
        if tree > mid:
            total += tree - mid
    
    if total < M:
        # 너무 덜 잘림 → 절단기 높이를 낮춰야 함
        return cut_trees(Sorted_Tree_List, M, start, mid - 1, result)
    else:
        # 충분히 잘렸음 → 절단기 높이를 올려도 됨
        return cut_trees(Sorted_Tree_List, M, mid + 1, end, mid)

answer = cut_trees(Tree_list, M, 0, max(Tree_list))
print(answer)