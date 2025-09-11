num1 = int(input())
num2 = int(input())
num3 = int(input())
app = num1 * num2 * num3

arr = list(map(int, str(app)))
cnt_1 = [0] * 10 

for ex_num in arr:
    cnt_1[ex_num] += 1 
    
for c in cnt_1:
    print(c)