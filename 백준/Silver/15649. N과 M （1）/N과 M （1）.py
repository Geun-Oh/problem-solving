import sys
import itertools
input = sys.stdin.readline
# input = open("test.txt").readline
# 사전식 정렬 + 백트래킹

n, m = list(map(int, input().split()))

def backtrack(arr, cnt):
    if cnt == m:
        print(" ".join(map(str, arr)))

    for i in range(1, n + 1):
        if i not in arr:
            backtrack(arr + [i], cnt + 1)

backtrack([], 0)