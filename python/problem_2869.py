# # 달팽이는 올라가고 싶다
# A, B, V = map(int, input().split())
# h = 0 # 달팽이가 이동한 거리
# cnt_date = 1
# while True:
#     h += A
#     if h < V:
#         h -= B
#         cnt_date += 1
#         print(cnt_date)
#     elif h >= V:
#         print(cnt_date)
#         print("달팽이가 정상에 도달함")
#         break

A, B, V = map(int, input().split())
print((V - B + (A - B) - 1) // (A - B))