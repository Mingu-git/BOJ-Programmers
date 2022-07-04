#-*- coding:utf-8 -*-

import sys
import heapq
input = sys.stdin.readline


"""
마찬가지로 최소값을 연속 연산한다는 점에서 heapq를 사용
"""
N = int(input())


for _ in range(N):
    K = int(input())
    arr = list(map(int,input().rstrip().split()))
    heapq.heapify(arr)
    ans = 0
    while len(arr) != 1:
        temp_A = heapq.heappop(arr)
        temp_B = heapq.heappop(arr)
        ans = ans + temp_A + temp_B
        heapq.heappush(arr,temp_A + temp_B)
    print(ans)
    

    