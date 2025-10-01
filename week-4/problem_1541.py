import sys
input = sys.stdin.readline

expr = str(input().strip())
minus_groups = expr.split('-')
group_sums = [sum(map(int, g.split('+'))) for g in minus_groups]
min_value = group_sums[0] - sum(group_sums[1:])

print(min_value)
