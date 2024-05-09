import re

n = int(input())

p = re.compile('^(100+1+|01)+$')

for i in range(n):
    if len(p.findall(input())) == 0:
        print("NO")
    else:
        print("YES")