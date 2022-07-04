#-*- coding:utf-8 -*-

import sys
import heapq
input = sys.stdin.readline

N = int(input())


arr = [ list(map(int, input().rstrip().split() )) for _ in range(N) ]

arr = sorted(arr, key = lambda x : x[0])



"""
만약에  3 5 3 이라면   거리는 각각 d = 3 + 0 + 3

3 3 5 3 3  for 거리 x 인원 = > 6 + 3 + 0 + 3 + 6 = d   or 3 3 0 3 3 인지..

야기서 d 값이 어떻게 하면 최소가 될것인가??  ==> 아이디어를 생각해봐야함!!

-> 하나씩 검사를 해도 될까..?  => N = 10 ^5 

+@ 답이 여러개 위치가 가장작은것 = max(a,b)라고했을때 a 를 이어 가주면 된다는 말씀.

"""
population = 0

for i in arr:
    population += i[1]
    
temp = 0
ans = 0
mid = round(population / 2)

for i in arr:
    temp += i[1]
    if temp >= mid :
        ans = i[0]
        break
    
print(ans)
    
    





    