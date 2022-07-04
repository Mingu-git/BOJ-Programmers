#-*- coding:utf-8 -*-

import sys
input = sys.stdin.readline


"""
목표 : 최대한 많은 박스들을 배송

조건
1. 항상 일직선
2.
첫번째로는 최대 용량 만큼의 수를 넣어줘야됨 그리고 다시 그것을 뺴줘야함 이말은 즉슨
택배 = 상하차 큐가 필요함.. (a,b) 큐형식으로 계속 뺏다 넣어줬다  ==> hard 구현 

여기서 뭔가 더 이상적인 방법이 있을까..?

1. 비어있다면 무조건 채워햐하고
2. 따지는 것은 각 스테이션 마다 따져줘야된다고 생각
혹시나 하는것 -> 거리를 계산해서 거리가 짧은순서대로 배열 = 중간에 적재될시 손해가 날 수있는 경우의수가 발생

->>> 배송이 빠른것부터 순서대로 나열 해서 계산.
우선순위를 가지게하는거지


1 2 30  /// 남은것이 30

        /// 남은것 60 - 20
        
3 4  40 ///   남은것이 20 -20

         ///  남은것 60 - 20 = 40
         
          60

"""

N , C = list(map(int , input().rstrip().split()))
M = int(input())

dilivery = [list(map( int , input().rstrip().split())) for _ in range(M) ]
dilivery = sorted(dilivery , key = lambda x : x[1])

arr = [ C for _ in range(M+2)] # 1-5 까지 남은 양
ans = 0



for st,end,cnt in dilivery:
    
    
    
    temp = arr[st:end]
    #print(temp,cnt)
    if min(temp) >= cnt:
        for j in range(st,end):
            arr[j] -= cnt
        ans += cnt
    elif min(temp) > 0:
        for k in range(st,end):
            arr[k] -= min(temp)
        ans += min(temp)


    

print(ans)