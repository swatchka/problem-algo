import sys
input = sys.stdin.readline

first = 0
t = int(input())
list = [0] * (t+1)
people_list = []
for j in range(t):
    n = int(input())
    for i in range(n):
        start, end = map(int, input().strip().split())
        people_list.append((start, end))
        people_list.sort()
        
        first = people_list[0]
        
        # for q in range(len(people_list)):
        #     for person in people_list:
                
print(people_list)
print(people_list[0][1])
        
