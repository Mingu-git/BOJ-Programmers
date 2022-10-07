"""
문자열

문제분석:


1. 태그 기준으로 문자열을 나누어줘야함  --> 원하는 문자기준으로 나눈다..
--> 탐색해서 슬라이싱
1. 위치 찾아서 슬라이싱 ->너무 비효율적
2. 양끝이 존제한다는 것은 start - end

2. 공백 기준으로 나눔 

3.뒤집기

4.반환

배울점 

1: 상태 변이를 따지는건 항상 if 문 서열1위로 하는게 편할듯!!

2. 거꾸로 넣는다는것 =


"""

import sys
input = sys.stdin.readline

arr = str(input().rstrip())
arr = list(arr)
temp_arr = []
temp = ""
ans = ""

flag = 0



for i in arr:
    
    if not flag:
        if i == '<':
            flag = 1
            temp += i
        elif i ==" ":
            temp += i
            ans = ans + temp
            temp = ""
        else:
            temp = i + temp
        
    else:
        temp += i
        if i =='>':
            flag = 0
            ans += temp
            temp =""
            

            
print(ans+temp)
    

