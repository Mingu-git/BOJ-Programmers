#-*- coding:utf-8 -*-

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())

arr = [list(map(int,input().rstrip().split())) for _ in range(N)]

# 가장 효율적인 방법은 무엇일까 : 
# 1. 목적 : 가장 최소의 강의실 사용 
# 1.1 : 포인트 : 끝과 시작이 맞는것들을 연결해주는게 중요하다 생각  -> 시간낭비가없어 

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
            
            


    