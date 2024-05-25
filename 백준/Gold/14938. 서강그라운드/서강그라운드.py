import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n, m, r = map(int, input().split())

arr = list(map(int, input().split()))

INF = int(1e9)

dijk = [[INF] * (n + 1) for i in range(n + 1)]

for _ in range(r):
    a, b, i = map(int, input().split())
    dijk[a][b] = i
    dijk[b][a] = i

for i in range(1, n + 1):
    dijk[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dijk[i][j] = min(dijk[i][j], dijk[i][k] + dijk[k][j])

ans = 0

for i in range(1, n + 1):
    tar = dijk[i]
    temp = 0
    for j in range(1, n + 1):        
        if tar[j] <= m:
            temp += arr[j - 1]

    ans = max(ans, temp)

print(ans)