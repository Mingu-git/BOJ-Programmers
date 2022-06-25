#-*- coding:utf-8 -*-
import sys
import itertools
input = sys.stdin.readline


N = int(input())   # 배열의 길이
honey_spot = list(map(int,input().rstrip().split()))
prefix_sun = [0 for _ in range(N)]
arr = []
sum = 0


for i in range(N):
    if i == 0:
        prefix_sun[0] = honey_spot[0]
    else:
        prefix_sun[i] = prefix_sun[i-1] + honey_spot[i]
        
for i in range(N):
    prefix_sun[i] = prefix_sun[i] - honey_spot[0]
    

for i in range(1,N-1): # 구간별 합의 최대값 구현
    temp = prefix_sun[i-1] + (2 * (prefix_sun[N-1] - prefix_sun[i] ))
    arr.append(temp)

for i in range(1,N-1):
    temp = prefix_sun[N-1] - honey_spot[N-1] + honey_spot[i]
    arr.append(temp)

for i in range(1,N-1):
    temp = (2* honey_spot[0]) + (2* prefix_sun[i-1]) + (prefix_sun[N-1] - prefix_sun[i] - honey_spot[N-1])
    arr.append(temp)
    


if N == 3:
    print(2 * max(honey_spot))
else:
    print(max(arr))
