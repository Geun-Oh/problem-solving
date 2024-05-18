import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# for i in range(1, n + 1):
#     graph[i][i] = i

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, n + 1):
    ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)