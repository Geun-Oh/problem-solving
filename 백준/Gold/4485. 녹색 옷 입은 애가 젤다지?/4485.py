import heapq

INF = int(1e8)

def dijkstra(cost, graph, cnt):
    q = []
    heapq.heappush(q, [0, 1, 0, 0])
    heapq.heappush(q, [1, 0, 0, 0])

    l = len(cost)

    while q:
        a, b, lastA, lastB = heapq.heappop(q)

        if a < 0 or a >= l or b < 0 or b >= l:
            continue

        if cost[lastA][lastB] + graph[a][b] < cost[a][b]:
            cost[a][b] = cost[lastA][lastB] + graph[a][b]
            heapq.heappush(q, [a + 1, b, a, b]) 
            heapq.heappush(q, [a - 1, b, a, b]) 
            heapq.heappush(q, [a, b + 1, a, b]) 
            heapq.heappush(q, [a, b - 1, a, b]) 
        else:
            continue
        
    print(f'Problem {cnt}: {cost[l - 1][l - 1]}')

cnt = 1
while True:
    v = int(input())
    if v == 0:
        break

    cost = [[INF] * v for i in range(v)]

    graph = []

    for i in range(v):
        graph.append(list(map(int, input().split())))

    cost[0][0] = graph[0][0]

    dijkstra(cost, graph, cnt)
    cnt += 1