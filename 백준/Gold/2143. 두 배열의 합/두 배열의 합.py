import sys
from bisect import bisect_left, bisect
input = sys.stdin.readline
# input = open("test.txt").readline

tar = int(input())

a = int(input())
arrA = list(map(int, input().split()))
b = int(input())
arrB = list(map(int, input().split()))

sumA = arrA[:]
sumB = arrB[:]

for i in range(a - 1):
    for j in range(i + 1, a):
        sumA.append(sum(arrA[i:j]) + arrA[j])

for i in range(b - 1):
    for j in range(i + 1, b):
        sumB.append(sum(arrB[i:j]) + arrB[j])
    
sumB.sort()

cnt = 0

for x in sumA:
    target = tar - x
    r = bisect(sumB, target)
    l = bisect_left(sumB, target)
    cnt += r - l

print(cnt)