#-*- coding:utf-8 -*-

import sys
import heapq
input = sys.stdin.readline


N = int(input())
arr = [list(map(int,input().rstrip().split())) for _ in range(N)]

ans = []
arr.sort(key = lambda x : x[0])
heapq.heappush(ans,arr[0][1])

for i in range(1,len(arr)):
    
    if ans[0] <= arr[i][0]:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i][1])
    else:
        heapq.heappush(ans,arr[i][1])
    


print(len(ans))
            