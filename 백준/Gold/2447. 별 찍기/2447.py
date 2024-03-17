v = int(input())

graph = [["*"] * v for i in range(v)]

k = 1
cnt = 0

while True:
    if k == v:
        break
    k *= 3
    cnt += 1

def merge_sort(x, y, k):
    for i in range(x + k, x + 2 * k):
        for j in range(y + k, y + 2 * k):
            graph[i][j] = " "
    if k > 1:
        n = k // 3
        for i in range(3):
            for j in range(3):
                merge_sort(x + i * k, y + j * k, n)

merge_sort(0, 0, v // 3)

for i in range(v):
    print("".join(graph[i]))