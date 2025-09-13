N, C = map(int, input().split()) # N은 집의 갯수 C는 공유기 갯수
home_list = [0] * N

for i in range(0, N):
    home_list[i] = int(input()) 
    
# =========================== 값 입력 받기 ===========================

sorted_home_list = sorted(home_list) # 집 좌표 정렬

start = 1
end = max(sorted_home_list) - min(sorted_home_list)
# mid_home = (max(sorted_home_list) + min(sorted_home_list)) // 2


def can_install_wifi(homes, distance, target_count): 
    count = 1
    last = homes[0]
    for i in range(1, len(homes)):
        if homes[i] - last >= distance:
            count += 1
            last = homes[i]
    return count >= target_count


result = 0
while start <= end: # 이분탐색을 활용하여 
    mid_home = (start + end) // 2
    if can_install_wifi(sorted_home_list, mid_home, C):
        result = mid_home
        start = mid_home + 1
    else:
        end = mid_home - 1
    
print(result)
        


    