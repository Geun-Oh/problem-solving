import sys
input = sys.stdin.readline
# input = open("test.txt").readline
# 사전식 정렬 + 백트래킹

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def backtrack(start, dest, arr):
    # print(start, dest, arr)
    if len(arr) == 5:
        return 1
    
    if dest in arr:
        return 0

    for x in graph[dest]:
        arr.append(dest)
        t = backtrack(dest, x, arr)
        if t == 1:
            return 1
        arr.remove(dest)

    return 0

p = 0

for i in range(n):
    for j in graph[i]:
        k = backtrack(i, j, [i])
        if k == 1:
            p = 1
            break

print(p)