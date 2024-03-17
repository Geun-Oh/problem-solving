arr1 = input().strip()
arr2 = input().strip()

n = len(arr1)
m = len(arr2)

graph = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr1[i - 1] == arr2[j - 1]:
            graph[i][j] = graph[i - 1][j - 1] + 1
        else:
            graph[i][j] = max(graph[i][j - 1], graph[i - 1][j])

print(graph[n][m])