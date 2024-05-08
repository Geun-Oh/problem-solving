# input = open("test.txt").readline

n, m, iv = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 먼저 목표 지점을 찾자
# 인벤토리 수에 따라 달라지는데, 
# 평균을 먼저 구하고, 
# 그냥 이진탐색으로 맨 위가 256이고 맨 아래가 0이니까
# 해가지구 하면 안되나
# 만약 mid를 만들기 위한 인벤 수가 부족하면 바로 줄이고
# 인벤이 남게 되면 시간이 최소인지 확인해서 바로 올리고
# 확인할 때 이전 값보다 시간이 낮으면 오키

ans = [-1, -1]

def getTime(mid):
    big = 0
    small = 0
    for i in range(n):
        for j in range(m):
            if mid < graph[i][j]:
                big += graph[i][j] - mid
            else:
                small += mid - graph[i][j]
    
    if iv + big < small:
        return -1
    
    return big * 2 + small

for mid in range(257):
    t = getTime(mid)
    if t == -1:
        continue
    if ans[0] == -1:
        ans = [t, mid]
        continue
    if ans[0] > t:
        ans = [t, mid]
    elif ans[0] == t and ans[1] < mid:
        ans = [t, mid] 
print(ans[0], ans[1])