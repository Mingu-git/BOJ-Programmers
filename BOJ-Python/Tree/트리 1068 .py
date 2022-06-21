#-*- coding:utf-8 -*-
"""
요구조건 : 1.트리구조 생성 -> class + {} or list
2.삭제 ->Dfs
3. 리프노드 계산 ->경우의수 찾아서 if 문


문제풀이 : 1. 시간초과가남 why? i dont know

iimport sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,data):
        self.left = -1
        self.right =  -1
        self.data = data
        
tree = {}
ans = 0

N  = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
k  = int(input().rstrip())


for i in range(N):
    if arr[i] == -1:
        tree[i] = Node(i)
    else:
        tree[i] = Node(i)

        if tree[arr[i]].left == -1:
            tree[arr[i]].left = i
        elif tree[arr[i]].right == -1:
            tree[arr[i]].right = i



def dfs(node):
  node.data = -1  
  if node.left != -1:
    dfs(tree[node.left])
  if node.right != -1:
    dfs(tree[node.right])
              

dfs(tree[k])

for i in tree:
    if tree[i].data != -1 and tree[i].left == -1 :
    
        ans += 1
      

print(ans)
    
"""
        
#1068 트리

#문제풀이 1.트리 구조를 어캐구현 했더라?
#파이썬 트리구조 = 2차원배열 or  딕셔너리

import sys
input =sys.stdin.readline
from collections import deque

N = int(input().rstrip())
arr = deque([] for _ in range(N))
Node = list(map(int,input().rstrip().split()))
K = int(input().rstrip())
cnt = 0
root = -1

for i in range(N):
    if Node[i] == -1:
        root = i
    else:
        arr[Node[i]].append(i)

def dfs(node):
    global cnt
    if not arr[node]:
        cnt += 1
        return

    for j in range(len(arr[node])):
        if arr[node][j] == K:
            if len(arr[node]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(arr[node][j])
   

if K == root:
    print(0)
else:
    dfs(root)
    print(cnt)





