import sys
from collections import deque

# 위상정렬은 진입차수와 진출차수를 기준으로 생각한다.
# 진입차수가 0이어야 해당 노드를 모두 방문한 것이어서, 더 이상 신경쓰지 않고 지울 수 있다.

input = sys.stdin.readline
# input = open("test.txt").readline

r = int(input())

for _ in range(r):
    node, edge = map(int, input().split())
    cost = list(map(int, input().split()))
    graph = [[] for _ in range(node + 1)] # 그래프
    inDegree = [0 for _ in range(node + 1)] # 각 진입차수
    dp = [0] * (node + 1)

    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    
    ans = int(input())

    q = deque()
    for i in range(1, node + 1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = cost[i - 1]

    while q:
        v = q.popleft()
        for i in graph[v]:
            inDegree[i] -= 1
            dp[i] = max(dp[v] + cost[i - 1], dp[i])
            if inDegree[i] == 0:
                q.append(i)

    print(dp[ans])