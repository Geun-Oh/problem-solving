def dfs(graph, start, visited):
    visited[start] = True
    print(start)
    for a in graph[start]:
        if not visited[a]:
            dfs(graph, a, visited)