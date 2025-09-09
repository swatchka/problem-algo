# 골드바흐 추측
# for a in range(1, n+1):
#     if n%a==0:
#         cnt+=1
        
# print('prime number' if cnt == 2 else 'natural number')


# def check_prime(h):
#     if h < 2:
#         print("np")
#     else:
#         for i in range(2, int(h**0.5) + 1):
#             if h % i == 0:
#                 cnt = "np"
#                 print("np")
#                 break
#         else:
#             cnt = "p"
#             print("p")
            
# n = int(input())
# p = n - 2
# check_prime(p)
# if check_prime == "np":
#     p = n - 3
#     print(3)
#     check_prime(p)
#     if check_prime == "np":
#         p = n - 5   
#         print(5)



# 골드바흐 추측
def is_prime(x):
    # 2보다 작은 수는 소수가 아님
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:  # 나누어떨어지면 소수가 아님
            return False
    return True  # 끝까지 안 나누어지면 소수
prime_list = []
for l in range(10000):
    if is_prime(l) == True:
        prime_list[l] = l
    
t = int(input())
result = [0] * t
result2 = [0] * t
for i in range(t):
    n = int(input())
    found = False  # 소수 쌍을 찾았는지 여부 저장
    for diff in prime_list:
        p = n - diff  # 후보 소수 p
        if is_prime(p):  # p가 소수인지 확인
            q = n - p
            result[i] = q   # n = p + q 형태이므로 q 계산
            if is_prime(q):  # q도 소수인지 확인
                result2[i] = p 
                found = True  # 소수 쌍을 찾았으니 표시
                break
for k in range(t):
    if result[k] < result2[k]:
        print(result[k], result2[k])
    if result[k] >= result2[k]:
        print(result2[k], result[k])