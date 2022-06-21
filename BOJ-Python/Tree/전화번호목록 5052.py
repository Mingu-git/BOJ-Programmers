#-*- coding:utf-8 -*-
"""
요구조건 : pre


문제풀이 : 정렬후 앞뒤 문자열만 비교

이때 정렬시 알아서 해결이 된다.


"""

import sys
input = sys.stdin.readline

def solution(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            return
    print("Yes")
    
N = int(input().rstrip())
for _ in range(N):
    K = int(input().rstrip())
    arr = []
    for _ in range(K):
        arr.append(input().rstrip())
    arr.sort()

    solution(arr)
