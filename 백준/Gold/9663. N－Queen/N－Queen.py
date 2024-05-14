import sys
input = sys.stdin.readline
#input = open("test.txt").readline

n = int(input())

arr = [0] * (n + 1)
global cnt
cnt = 0

def isGood(x):
    for i in range(1, x):
        if arr[i] == arr[x] or abs(i - x) == abs(arr[i] - arr[x]):
            return False
    return True

def backtrack(x):
    global cnt
    if x == n + 1:
        cnt += 1
        return

    for i in range(1, n + 1):
        arr[x] = i
        if isGood(x) == True:
            backtrack(x + 1)

backtrack(1)

print(cnt)

