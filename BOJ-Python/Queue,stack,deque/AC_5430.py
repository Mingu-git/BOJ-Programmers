"""
스택 마지막문제 

how?

두가지 기능 R(뒤집기) + D(버리기)

배열이 비어있을 경우 D 불가능

1. 문자열 하나씩 쪼개기

"""


from curses.ascii import isdigit
import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
ans = []

for i in range(N):
    
    flag = 1
    func = list(str(input().rstrip()))
    fun = []
    
    M = int(input())
    
    arr =str(input())
    
    
    
    if len(arr) == 3:
        arr =[]
    else:
        arr= arr[1:len(arr)-2]
        arr = arr.split(",")

            
    arr = deque(arr)
    
    for j in func:
        if j =="R":
            fun.append("R")
        else:
            if len(arr) == 0 :
                flag = 0
                ans.append("error")
                break
            else:
                if len(fun) % 2 == 0 or len(fun) == 0 :
                    arr.popleft()
                else:
                    arr.pop()
                
    if flag:
        ans.append(list(arr))
    elif len(fun)%2 == 1:
        arr.reverse()
        ans.append(arr)
        
for i in ans:
    print(i)