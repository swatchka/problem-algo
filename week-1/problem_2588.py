# 곱셈 2588
num1 = int(input())
num2 = int(input())
num2_str = str(num2)
num2_list = []

for digit in num2_str:
    num2_list.append(int(digit))
    
l = len(num2_list)
for add in reversed(range(0, l)):
    if l < 2:
        pass
    else:
        print(num1 * num2_list[add])
print(num1 * num2) 