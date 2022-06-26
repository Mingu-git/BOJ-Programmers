#-*- coding:utf-8 -*-

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())

arr = [list(map(int,input().rstrip().split())) for _ in range(N)]

# 가장 효율적인 방법은 무엇일까 : 
# 1. 목적 : 가장 최소의 강의실 사용 
# 1.1 : 포인트 : 끝과 시작이 맞는것들을 연결해주는게 중요하다 생각  -> 시간낭비가없어 

# 하지만 포인트가 틀렸다.
#여기서 시간낭비는 신경쓰지 않고 오직 작은종료시간 값 하나만 비교해줌으로써 답을 도출.
# 가장 작은 시간을 효율적으로 도출해낸다 -> heapq의 주된 목적성을 가짐  : 이논리로 사용을 이끌어내야함.

ans = []
arr.sort(key = lambda x : x[1])
heapq.heappush(ans,arr[0][1])

for i in range(1,len(arr)):
    
    if ans[0] <= arr[i][0]:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i][1])
    else:
        heapq.heappush(ans,arr[i][1])
    


print(len(ans))
            
            


    