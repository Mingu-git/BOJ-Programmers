

import sys
input =sys.stdin.readline


#N= list(map(int,input().split()))
N , M = map(int , input().split())
pwd = str(input())

cnt = list(map(int , input().split()))
dic_cnt = {}
test_cnt = {}
ans = 0
dic = ['A','G','C','T']

for i in range(len(cnt)):
    dic_cnt[dic[i]] = cnt[i]
    test_cnt[dic[i]] = 0
    
"""
스택구조로 하나씩 더해야 제대로 진행된다고 생각

시간단축이 문제인대

않끈고 백만번하면되는데 최대의
"""

def check(arr1 ,arr2):
    temp = ['A','G','C','T']
    for i in range(4):
        if arr1[temp[i]] > arr2[temp[i]]:
            return False
    return True
        

# 초기 설정
st = pwd[:M]
for i in st:
    test_cnt[i] += 1
    
if check(dic_cnt , test_cnt):
    ans += 1


start = 0
for i in range(M, len(pwd)-1):
    

    temp = pwd[i]
    temp2 = pwd[start]
    test_cnt[temp] += 1
    test_cnt[temp2] -= 1
    if check(dic_cnt , test_cnt):
        ans += 1
        
    start += 1
print(ans)