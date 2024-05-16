import sys
input = sys.stdin.readline
# input = open("test.txt").readline

r = int(input())

for _ in range(r):
    n = int(input())
    arr = list(map(int, input().split()))
    tar = int(input())

    dp = [[0] * (tar + 1) for i in range(len(arr) + 1)]

    for k in range(len(arr) + 1):
        dp[k][0] = 1

    for j in range(1, len(arr) + 1):
        for i in range(1, tar + 1):
            dp[j][i] = dp[j - 1][i]
            if i - arr[j - 1] >= 0:
                dp[j][i] += dp[j][i - arr[j - 1]]

    print(dp[len(arr)][tar])