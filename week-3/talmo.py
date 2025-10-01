n = int(input())
def pibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pibo(n-1) + pibo(n-2)
    
print(pibo(n))