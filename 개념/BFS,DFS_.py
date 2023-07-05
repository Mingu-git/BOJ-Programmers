"""
bfs / dfs 탐색


"""

 

1. DFS -
    a. 주로 완전 탐색 및 끝까지 내려가서 특정 조건을 만족하는 것을 찾기 위해 사용됨
    b. 주로 recursion구조를 활용하여 사용됨
    c. recursion의 경우 가장 중요한것 ==>  1. 인자 (def(a,b)) 2. return 분기점 3.visited의 활용
    
    
2. BFS-
    a. 주로 최선의 값을 도출할때 효율적. 쓰레기값 까지 다 탐색하지 않고 천천히 넓혀 가기때문에 "최단거리"와 같은 
    문제를 다룰때 용이
    b. 주로 while + deque + "4방향" 구조를 활용하여 구현됨 . 따라서 스택에 pop / push 구조를 활용하여 전체적으로 탐색
    
    c. 빈출 유형 
        1. 최단거리탐색 : 이와같은 유형은 주로 4방향을 탐색하며 각종 조건들을 활용하여 문제 조건을 풀이
        특히나 이전 최단 거리값을 활용하기 위해 arr[nx][ny] = arr[x][y] + k 와 같이 이전 값이 최선의 값이라는
        것을 활용하여 구현한다면 쉬움
        
        2.
    
    
3. +@
    a. dfs시 하나의 list를 가지고 쭉이어가면 같은 참조값을 가지기 때문에 비교를 하기에 용이하지 않다.
    따라서 편하게 비교하기 위해 "copy , [:]"와 같은 것들을 활용하여 비교해보기
    
    b. extend = 주로 [a,b]와 같이 list로 묶여져 있는 인자들을 편하게 정답 배열에 넣기 위해 사용됨
    
    c. 루트 노드 -> 자식노드 -> 루트 노드 == 이러한 순환성은 추후 방문한 것을 기준으로 생각해봤을때
    서로의 값이 같다느 것을 활용하여 풀어낼 수 있다.
    
    
"토마토"

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


"숨바꼭질"
from collections import deque
MAX = 100001
check = [False] * MAX
dist = [-1] * MAX

n,k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 <= MAX and check[now*2] == False:  # 순간이동
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 <= MAX and check[now+1] == False: # x+1이동
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and check[now-1] == False: # x-1이동
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
print(dist[k])

"숫자고르기"
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(1, N+1):
    temp = int(input())
    graph[i].append(temp)


def dfs(n):
    if not visited[n]:
        visited[n] = True
        for i in graph[n]:
            mother.add(n)
            child.add(i)
            if mother == child:
                cycle.extend(mother)
                return
            dfs(i)


cycle = []

for i in range(1, N+1):
    visited = [False] * (N + 1)
    mother = set()
    child = set()
    dfs(i)

cycle = list(set(cycle))
cycle.sort()

print(len(cycle))
print('\n'.join(str(i) for i in cycle))

dfs(1)

"산책(small)"