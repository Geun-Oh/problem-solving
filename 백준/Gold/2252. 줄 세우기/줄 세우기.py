import sys
from collections import deque
input = sys.stdin.readline
# input = open("test.txt").readline

n, m = map(int, input().split())


graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)

ans = []

while q:
    x = q.popleft()
    ans.append(x)
    for v in graph[x]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
            q.append(v)

print(" ".join(map(str, ans)))