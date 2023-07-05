from collections import defaultdict
from collections import deque
import re
import sys
from unittest import result

input = sys.stdin.readline  # 입력

N , M = map(int , input().split()) #  N = 컴 갯수 / M = 줄갯수
comp = [[] for _ in range(N + 1)]#컴퓨터 
temp_ans = defaultdict(list)  # 답안 
ans = []

for i in range(M):
	N,M = map(int , input().rstrip().split())
	comp[M].append(N)


flag = [ 0 for _ in range(N+1) ]

def bfs(start):
    q = deque()
    q.append(start)
    visited = [ 0 for _ in range (N+1)]
    visited[start] = 1
    cnt = 1
    
    while q:
        st = q.popleft()
        for i in comp[st]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt
max_cnt = 0
result = []

for i in range(1, N+1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    elif max_cnt < tmp:
        max_cnt =tmp
        result = [i]

print(*result)