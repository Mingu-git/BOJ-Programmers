from collections import defaultdict
from collections import deque
from itertools import combinations
from socket import EAI_SYSTEM

import  sys
from tkinter.tix import Tree
input = sys.stdin.readline



N , M=  list(map(int, input().split()))

tomato = []
value = False
for _ in range(M):
    temp = list(map(int , input().split()))
    if 0 in set(temp):
        value = True
    tomato.append(temp)
    
ans = 0

#인접한곳에 익지 않은 것들 -> 익은 토마토 근처에 있을시 익게됨 -> bfs

# 인접 4개의방향을 듯함

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 최소 일 수를 알고 싶다 -> bfs로 빠르게 구현 가능

############여기 까지 문제파악

##### 출력 조건 및 특정 조건 확인

# 1. -1은 토마토가 들어있지 않은것 / 0 은 익지 않은 토마토 
# 2. 모든 토마토가 익어 있는 상태라면 0 출력 ==> 0이 한개도 없는 상태라면 바로 0 출력
# 3. 토마토가 모두 익지 못하는 상황이면 -1 출력  ==> bfs를 다돌린후 0 이 존재시 -1 출력
# 4. 이외의 경우에는 최단 일수 출력
# 3과 4번은 같이 가는것

# 무엇을 인자로 넘겨야 될까 ==> 처음 시작위치  이지 않을까
from collections import deque
m,n = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(m): #익은 토마토 큐에 저장
        if graph[i][j]==1:
            queue.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m and graph[a][b]==0:
                queue.append([a,b])
                graph[a][b] = graph[x][y]+1
bfs()
answ = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))
print(answ-1)
