"""
문자열

파일정리

문제 분석

1. .이후 문자열 분리
split사용

2. 사전순 정렬


"""

import sys
input = sys.stdin.readline


N = int(input())
temp = []
ans = {}

for i in range(N):
    a , b = input().rstrip().split(".")
    
    if b in ans:
        ans[b] = ans[b] + 1
    else:
        temp.append(b)
        ans[b] = 1
        
temp = sorted(temp)

for i in temp:
    print(i , ans[i])
    

    
    
