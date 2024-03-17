input = open('test.txt').readline

import sys
sys.setrecursionlimit(10001)

tree = []
answer = []

while True:
    try:
        v = int(input())
        tree.append(v)
    except:
        break
        
def BST(arr):
    if len(arr) != 0:
        answer.insert(0, arr[0])
    if len(arr) <= 1:
        return
    idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[0]:
            idx = i
            break
    if idx == 0:
        BST(arr[1:]) 
        return
    BST(arr[idx:])
    BST(arr[1:idx])


BST(tree)

for i in range(len(answer)):
    print(answer[i])