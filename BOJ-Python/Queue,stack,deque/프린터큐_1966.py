#-*- coding:utf-8 -*-

"""
rotate 정도만 알아놓자. or deque의 다른 함수들 까지
"""

from collections import deque
count = int(input().strip())


for i in range(count):
    N,M = map(int,input().split())
    arr = deque(list(map(int, input().split())))
    ans =0

    while 1:
        if arr[0] == max(arr):
            if M ==0:
                ans =ans +1
                print(ans)
                break
            else:
                arr.popleft()
                ans = ans+1
                M = M-1
        else:
            arr.rotate(-1)
            if M>0:
                M = M-1
            else:
                M = M+len(arr)-1


