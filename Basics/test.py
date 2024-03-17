input = open("test.txt").readline

n, r, q = map(int, input().split())

# parent = [] * (n + 1)
graph = [[] for i in range(n + 1)]

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(x)
#     return parent[x]

# for i in range(n + 1):
#     parent[i] = i

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

def deep(start, node, count):
    if len(graph[node]) == 1:
        count += 1
        return count
    else:
        for i in graph[node]:
            if i != start:
                count += deep(node, i, count)


for i in range(q):
    count = 1
    v = int(input())
    for j in graph[v]:
        deep(v, j, count)