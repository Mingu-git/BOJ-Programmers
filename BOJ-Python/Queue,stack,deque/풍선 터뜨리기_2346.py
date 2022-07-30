#-*- coding:utf-8 -*-

import sys
input = sys.stdin.readline
from collections import deque


N = int(input().rstrip())
arr = list(map(int,input().split() ))

arr = deque(arr)
arr2 = deque([i for i in range(1,N+1)])
ans = []
st = 0

while arr:
    
    temp = arr[0]
    ans.append(arr2[0])
    if len(ans) == N:
        break
    arr.popleft()
    arr2.popleft()
    
    if temp >0:
        arr.rotate(-temp+1)
        arr2.rotate(-temp+1)
    else:
        arr.rotate(-temp)
        arr2.rotate(-temp)

for i in ans:
    print(i , end = " ")