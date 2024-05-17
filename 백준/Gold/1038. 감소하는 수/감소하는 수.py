import sys
import itertools
input = sys.stdin.readline
# input = open("test.txt").readline
# 사전식 정렬 + 백트래킹

n = int(input())

arr = []

def reform(x):
    a = list(x)
    a.sort(reverse = True)
    return int("".join(map(str, a)))
if n > 1022:
    print(-1)
else:
    i = 1
    while True:
        arr = list(itertools.combinations([j for j in range(10)], i))
        narr = list(map(reform, arr))
        narr.sort()
        if len(narr) > n:
            print(narr[n])
            break
        else:
            n -= len(narr)
            i += 1