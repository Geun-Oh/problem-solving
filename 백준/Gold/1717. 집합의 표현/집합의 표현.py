import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# input = open("test.txt").readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

for _ in range(m):
    o, a, b = map(int,input().split()) # operation, 원소, 원소
    if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
        union(a,b)
    elif o == 1: # 두 원소가 동일한 집합인지 판단
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')

# arr = []


# for _ in range(m):
#     x, a, b = map(int, input().split())
#     if x == 0:
#         union(a, b)
#         continue
#     if x == 1:
#         arr.append([a, b])

# for k in arr:
#     a, b = k
#     if find_parent(a) == find_parent(b):
#         print("YES")
#     else:
#         print("NO")