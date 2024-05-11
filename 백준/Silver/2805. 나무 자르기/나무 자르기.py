import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))
# M에 대해서 이진 탐색을 진행한다.

def getTree(k):
    cnt = 0
    for i in trees:
        if i > k:
            cnt += (i - k) 
    return cnt

l = 0
r = max(trees)

while l < r:
    mid = (l + r) // 2
    t = getTree(mid)
    
    if t < m:
        r = mid
    else:
        l = mid + 1

print(l - 1)