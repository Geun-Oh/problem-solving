input = open('test.txt').readline

n, m = map(int, input().split())
k = int(input())
INF = 1e8
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, node = heapq.heappop(q)

        if distance[node] < dis:
            continue

        for i in graph[node]:
            if dis + i[1] < distance[i[0]]:
                distance[i[0]] = dis + i[1]
                heapq.heappush(q, (dis + i[1], i[0]))

dijkstra(k)

print(distance)