#-*- coding:utf-8 -*-
"""
요구조건 :  

1. 

"""

import sys
input =sys.stdin.readline

N=int(input()[0:-1])
li = list(map(int, input()[0:-1].split()))
reverse = li[::-1]


increase = [ 1 for _ in range(N)]
decrease = [ 1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if li[i] > li[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse[i] > reverse[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for _ in range(N)]

for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] -1

print(max(result))