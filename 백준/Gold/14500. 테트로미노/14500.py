from collections import deque

input = open('main.txt').readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def getMidSum(start, visited, graph):
    t = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    v = [0, 0]

    for p in t:
        y, x = p
        if start[0] + y < 0 or start[0] + y >= n or start[1] + x < 0 or start[1] + x >= m:
            continue
        if visited[start[0] + y][start[1] + x] == True:
            t.remove([y, x])
            v = [y, x]

    sy, sx = start

    a = -1001 
    b = -1001
    c = -1001
    center = -1001
    notCenter = []

    if sy + t[0][0] < 0 or sy + t[0][0] >= n or sx + t[0][1] < 0 or sx + t[0][1] >= m:
        pass
    else:
        a = graph[sy + t[0][0]][sx + t[0][1]]
        if t[0][0] + v[0] == 0 and t[0][1] + v[1] == 0:
            center = a
        else:
            notCenter.append(a)

    if sy + t[1][0] < 0 or sy + t[1][0] >= n or sx + t[1][1] < 0 or sx + t[1][1] >= m:
        pass
    else:
        b = graph[sy + t[1][0]][sx + t[1][1]]
        if t[1][0] + v[0] == 0 and t[1][1] + v[1] == 0:
            center = b
        else:
            notCenter.append(b)

    if sy + t[2][0] < 0 or sy + t[2][0] >= n or sx + t[2][1] < 0 or sx + t[2][1] >= m:
        pass
    else:
        c = graph[sy + t[2][0]][sx + t[2][1]]
        if t[2][0] + v[0] == 0 and t[2][1] + v[1] == 0:
            center = c
        else:
            notCenter.append(c)

    new = max(notCenter) + center

    return new

def bfs(graph, start):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    queue.append([start[0] + 1, start[1], 2, graph[start[0]][start[1]]])
    queue.append([start[0] - 1, start[1], 2, graph[start[0]][start[1]]])
    queue.append([start[0], start[1] + 1, 2, graph[start[0]][start[1]]])
    queue.append([start[0], start[1] - 1, 2, graph[start[0]][start[1]]])
    k = 0
    while queue:
        y, x, c, s = queue.popleft()

        if y < 0 or y >= n or x < 0 or x >= m:
            continue
        if visited[y][x] == True:
            continue
        if c > 4:
            k = max(k, s)
            continue
        s += graph[y][x]    
        if c == 2:
            z = getMidSum([y, x], visited, graph)
            k = max(k, z + s)
        c += 1
        visited[y][x] = True

        queue.append([y + 1, x, c, s])
        queue.append([y - 1, x, c, s])
        queue.append([y, x + 1, c, s])
        queue.append([y, x - 1, c, s])

    return k

ans = 0

for i in range(n):
    for j in range(m):
        t = bfs(graph, [i, j])
        ans = max(ans , t)

print(ans)