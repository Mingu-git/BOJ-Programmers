"""
문자열

문제 분석

필요한게없음
"""

import sys
input = sys.stdin.readline

from collections import defaultdict


temp = set()
ans = []

N,M = map(int,input().split())

for i in range(N):
    temp.add(input().rstrip())

for j in range(M):
    temp_word = input().rstrip()
    if temp_word in temp:
        ans.append(temp_word)
        
print(len(ans))

for i in sorted(ans):
    print(i)
    
