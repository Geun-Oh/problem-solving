from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

