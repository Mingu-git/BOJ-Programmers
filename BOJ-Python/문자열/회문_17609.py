"""

문자열

팰린드롬

투포인트를 써서 확인을 할 순있어

그와중에 발생하는 예외들을 관리하기가 어려워

여기서는 많은경우의수를 포함할 수 있는 분기문만드느냐??

아니면 내가 놓치고 있는 포인트가 있느냐 

2가지일꺼같아


"""

import sys
input =sys.stdin.readline


N = int(input().rstrip())
ans = []

for _ in range(N):
    
    word = list(str(input().rstrip()))
    flag = 1
    
    if word == word[::-1]:
        ans.append(0)
    else:
        
        start = word
        end = word
        
        leng = int(len(word) // 2)
        
        
        for i in range(leng):
            
            
            if word[i] != word[-(i+1)]:
                
                start.pop(i)
                end.pop(-(i+1))

                if start == start[::-1]:
                    ans.append(1)
                    flag = 0
                    break
                
                if end == end[::-1] and flag:
                    ans.append(1)
                    flag = 0
                    break
                
                if  flag:
                    ans.append(2)
                    break

print(ans)


