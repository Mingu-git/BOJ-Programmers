"""
문자열

1316 그룹체커

요구조건 : 그룹단어의 갯수출력

그룹단어 조건

1: 이어져 있어야함
만약에 이미 그 문자가 있다면 그룹조건이 아님

따라서 set + in 사용 좋을듯

배울점 :

1. set - in 단축 굿

2.연속성 : 이전 것과 비교 하여 진행

"""


import sys
input = sys.stdin.readline


N = int(input())
arr = []

ans = 0

for i in range(N):
    arr.append(input().rstrip())

for i in arr:
    arr2 = list(i)
    flag = 1
    temp =set()
    
    for j in range(len(arr2)):
        
        if arr2[j] not in temp:
            
            temp.add(arr2[j])
        else:
            if arr2[j] != arr2[j-1]:
                flag = 0
                break
        
    if flag:
        ans += 1
        
print(ans)