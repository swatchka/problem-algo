# # 첫번째 입력으로 종이의 크기 정의
# # 두번째 입력으로 몇번 자를지 입력
# # 자를 좌표 지정
# import numpy as np


# x, y = map(int, input().split())

# filled_arr = np.full((y + 1, x + 1), "■", dtype=str)

# print("\n초기 배열:")
# for row in filled_arr:
#     print(" ".join(row))

# t = int(input())
# for _ in range(t):
    
#     cut_x, cut_y = map(int,input().split())

#     empty_row = np.full((1, filled_arr.shape[1]), " ", dtype=str)
#     empty_col = np.full((filled_arr.shape[0] + 1, 1), " ", dtype=str)
#     if cut_y > 0:
#         filled_arr = np.vstack([filled_arr[:cut_y], empty_row, filled_arr[cut_y:]])
#     else:
#         filled_arr = np.vstack([empty_row, filled_arr])

#     if cut_x > 0:
#         filled_arr = np.hstack([filled_arr[:, :cut_x], empty_col, filled_arr[:, cut_x:]])
#     else:
#     filled_arr = np.hstack([empty_col, filled_arr])

#     # print("\n잘린 배열:")
# for row in filled_arr:
#     print(" ".join(row))
# print(filled_arr)

# def cut_lines(arr, cut_sym = " "):
#     row_cuts = []
#     col_cuts = []
#     for i in range(arr.shape[0]):
#         if np.all(arr[i] == cut_sym):
#             row_cuts.append(i)
            
#     for j in range(arr.shape[1]):
#         if np.all(arr[:, j] == cut_sym):
#             col_cuts.append(j)
         
#     return row_cuts, col_cuts
#     # 세로줄(열 단위)
    
# rows, cols = cut_lines(filled_arr)

# max_x = rows[0] - x
# max_y = cols[0] - y
# print(abs(max_x))
# print(abs(max_y))

