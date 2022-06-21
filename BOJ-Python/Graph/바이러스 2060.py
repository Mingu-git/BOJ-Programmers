#-*- coding:utf-8 -*-
"""
요구조건 :  1. 주어진 자료를 통해 그래프 구조형성

2.연결되어있는 모든 노드를 탐색 

"""


import sys
input = sys.stdin.readline

n  = int(input().rstrip())

v = int(input().rstrip())

# 중복 제거 set
arr = [[] for _ in range(n+1)]
visited = [ False for _ in range((n+1))]  # 무방향이기때문에 무환 루프를 돌수있기에 구현
ans = 0
temp = 0
for i in range(v):
    
    a,b = map(int , input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

# 그래프 중 무방향 그래프 따라서 각노드에 넣어줌
    


def dfs(cnt):
    global ans
    visited[cnt] = True
    for i in arr[cnt]:
        if not visited[i] :
            dfs(i)
            ans += 1
# 완전 탐색

dfs(1) 
print(ans)

    
    