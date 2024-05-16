import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n, k = map(int, input().split())

dp = [100001] * (100001)

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

newArr = list(set(arr))

for x in newArr:
    dp[x] = 1

for i in range(1, k + 1):
    for x in newArr:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])