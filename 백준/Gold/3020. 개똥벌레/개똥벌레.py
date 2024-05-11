import sys
input = sys.stdin.readline
# input = open("test.txt").readline

n, h = map(int, input().split())

bottom = []
top = []
bot = True
for _ in range(n):
    if bot == True:
        bottom.append(int(input()))
        bot = False
    else:
        top.append(int(input()))
        bot = True

top.sort()
bottom.sort()

def lower_bound(array, target):
    l, r = 0, len(array)

    while l < r:
        mid = (l + r) // 2

        if target <= array[mid]:
            r = mid
        else:
            l = mid + 1

    return l

arr = [0] * (h)

for i in range(1, h + 1):
    arr[i - 1] = n - (lower_bound(bottom, i) + lower_bound(top, h - i + 1))

print(min(arr), arr.count(min(arr)))