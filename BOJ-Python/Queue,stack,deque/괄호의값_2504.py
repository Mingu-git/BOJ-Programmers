#-*- coding:utf-8 -*-
"""
이 문제에서의 배울점은

후위, 전위 ,??? 표기식에서의 스택논리구조를 이해하자.

이 문제같은경우에는 끝맺음을 기점으로 연산을 마무리하였다기보다

시작부분에서 미래에 올 계산들을 유추하는기법. 괄호 연사에좀 가깝다. 따라서 괄호에따라 우선순위가 바뀔때

이러한 방식으로 접근하면 좋을꺼같다.
"""
import sys
input = sys.stdin.readline
from collections import deque


arr = list(input().rstrip())
temp_X = []
temp_Y = []
temp = 1
ans = 0
ispaired = True

for i in range(len(arr)):
    if arr[i] == '(':
        temp_X.append(arr[i])
        temp *= 2
    
    elif arr[i] =='[':
        temp_Y.append(arr[i])
        temp *= 3
    
    elif arr[i] == ')':
        if temp_X:
            if arr[i-1] =='(':
                ans += temp
            temp_X.pop()
            temp //= 2
            
        else:
            ispaired = False
            break
    elif arr[i] == ']':
        if temp_Y:
            if arr[i-1] =='[':
                ans += temp
            temp_Y.pop()
            temp //= 3
        else:
            ispaired = False
            break
        

if not temp_X and not temp_Y and ispaired:
    print(ans)
else:
    print(0)
    


