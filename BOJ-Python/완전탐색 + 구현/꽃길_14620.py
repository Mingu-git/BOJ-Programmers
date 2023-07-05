
"""

2023.05.14

문제 : 어떻게 하면 cost로 구현할 수 있는가..?

1. 해결 제시책 : 들어갈 수 있는 모든 경우의 수를 넣어준후 답을 구한다

==> Brute Force : ???

콤비내이션 활용 한번 먼저 해보자

2. 백트랙킹 : 이전에 구한값이 아니라면 돌아가서 다시 시작 == dfs + 초기화라고도 할 수 있다고봄

==> 백트랙킹 : ???

"""

#1번 : combinations을 통한 풀이

"""




import sys
from itertools import combinations, permutations, product
input = sys.stdin.readline


N = int(input())
cost = []
ans = 9999999

for _ in range(N):
    temp = list(map(int, input().rstrip().split()))  # 각각의 cost을 입력해서 넣어줘여함~
    cost.append(temp)
    

# 후보자들은 어떤게 들어가야 될까..? 일단 테두리 에있는것들은 다안됨 따라서
# N=6 이라고 한다면  0 1 2 3 4 5 일텐대 이렇게 되면 1 ,2 , 3, 4가 되어야함
candidates = []
for i in range(1,N-1):
    for k in range(1,N-1):
        
        candidates.append([i,k])

# 검증 머신 
# 꽃이 무조건 다펴야 되는것이니까 피는것들 만 합산을 해서 ans값에 넣어주는것
# ans값이러면 알아서 업데이트 되나?
def check(arr):
    temp = 0
    global ans
    
    # visited 구현해줘서
    # 각각 방문해주고 아닐 시 return
    # 될시 값 update
    
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dir_x = [0,1,-1,0]   # 
    dir_y = [1,0,0,-1]
    for x,y in arr:
        
        if visited[x][y] == 0:
            for i in range(4):
                dx = x + dir_x[i]
                dy = y + dir_y[i]
                
                if visited[dx][dy] == 1:
                    return 
                
                visited[dx][dy] = 1
                temp += cost[dx][dy]
            visited[x][y] = 1
            temp = temp + cost[x][y]
        else:
            return
    
    #print(temp , arr)
    ans = min(temp , ans)
    return 0


for li in combinations(candidates, 3):
    #print(li)
    check(li) 


print(ans)

"""


#2번 : 백 트랙킹을 통한 풀이

import sys
input =sys.stdin.readline

N = int(input())
cost = []
ans = 999999999
for _ in range(N):
    temp = list(map(int , input().split()))
    cost.append(temp)
    
visited = [[0 for _ in range(N)] for _ in range(N) ]
dir_x = [0 , 1, -1 , 0]
dir_y = [1 , 0 , 0 , -1]
# 백 트랙킹을 한다는것 -> 어느조건에서 dfs를 return 하겠다는 것

# dfs를 다루다 보면 기본에 우리가 다루던 지표들이 망가지게 되는데

# 이를 복구하는 방법  1 . 큰 분기에서 지표를 초기화 해준다.
# dfs  1. 인자 2. 리턴 3. visited  이 3개가 큰 지표
def check(temp, N):
 
    return 0

def dfs(arr , cnt , price):
    global ans
    print("!@#!@#!#!@#!@#")
    print(arr, cnt , price )
    
    if cnt == 3 or price > ans:
        ans = min(ans , price)
        return
    # 0  과 경계는 의미 없으니까
    for x in range(1,N-1):
        for y in range(1,N-1):
            print(x,y)
            
            if arr[x][y] == 0:
                arr[x][y] = 1
                
                for i in range(4):
                    dx = x
                    dy = y
                    dx += dir_x[i]
                    dy += dir_y[i]
                    
                    if arr[dx][dy] == 1:
                        return
                    arr[dx][dy] = 1
                    price += cost[dx][dy]
                    
                price +=  cost[x][y]
                
                #print(price , arr)
                
                dfs(arr , cnt+1 , price )
                
                arr[x][y] = 0
                for i in range(4):
                    arr[x+dir_x[i]][y+dir_y[i]] = 0
            
                 
                
            
            
  
    
    return 0 
#print(visited)
dfs(visited , 1 , 0 )  
print(ans)