#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

"""
풀이
1: 전제조건 보는것이 매우중요했음 -> 모든나라가 연결 되어있다. => 1->10 경로존재
2: 최소값 구할려고 시간낭비했음.


"""

T = int(input().rstrip())

#인접리스트
while T:
    T -= 1
    N,M = map(int,input().rstrip().split())
    
    arr = [[]  for _ in range(N+1)]
    for _ in range(M):
        a , b = map(int,input().rstrip().split())   
        arr[a].append(b)
        arr[b].append(a)
        
    print(N-1)
    
