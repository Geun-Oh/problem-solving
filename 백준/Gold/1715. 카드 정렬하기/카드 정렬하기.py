import heapq

import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

heapq.heapify(arr)
# 합친 카드 수를 기준으로 해서 4장을 합친 최소를 구하려면 3장을 합친 최소가 이미 있다고 할 때,
# 3장을 합친 최소
cnt = 0
s = 0
while len(arr) > 1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    cnt += (x + y)
    heapq.heappush(arr, x + y)

print(cnt)