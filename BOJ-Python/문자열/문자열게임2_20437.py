"""
문자열 뒤집기

문제 분석.

특정배열에서

임의문자 + 갯수

가장 짧은것
가장 긴것


관건 : 임의 문자 처리 방식
1. table 형태

2. 가장큰 제약이 맨끝에 있어야함 -> st , end 길이가 중요.

배울점

from collection import defauldict

arr = defaultdict(list)

2차원 배열과 같음 사실상

"""

from collections import defaultdict
import sys


input =sys.stdin.readline

N=int(input())


for i in range(N):
    
    word = list(str(input()))
    K = int(input())
    temp = defaultdict(list)
    ans=[]
    for i in range(len(word)):
        temp[word[i]].append(i)
        if len(temp[word[i]]) == K:

            ans_temp = temp[word[i]][-1] - temp[word[i]][0]
            ans.append(ans_temp+1)
            temp[word[i]].pop(0)
    if ans:
        print(min(ans),max(ans))
    else:
        print(-1)