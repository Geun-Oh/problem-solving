import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n = int(input())

arr = [501] * 502

dp = [0] * 502

for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b

for i in range(1, 502):
    for j in range(1, i):
        if arr[i] - arr[j] > 0:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))