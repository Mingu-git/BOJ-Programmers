"""

문자열

팰린드롬

투포인트를 써서 확인을 할 순있어

그와중에 발생하는 예외들을 관리하기가 어려워

여기서는 많은경우의수를 포함할 수 있는 분기문만드느냐??

아니면 내가 놓치고 있는 포인트가 있느냐 

2가지일꺼같아

이문제의 포인트 : 


"""

import sys
input =sys.stdin.readline

N = int(input())
ans = []

for _ in range(N):
    
    word = str(input().rstrip())
    word_temp = list(word)
    
    if word == word[::-1]:
        ans.append(0)
    else:
        
        st_word = list(word_temp)
        end_word =list( word_temp)
        L = len(word_temp) // 2
        
        #print(st_word ,end_word)
        
        for i in range(L):
            #print(word_temp[i] , word_temp[-(i+1)])
            if word_temp[i] != word_temp[-(i+1)]:
                
                st_word.pop(i)
                end_word.pop(-(i+1))
                #print(i,st_word,end_word)
                if st_word == st_word[::-1]:
                    ans.append(1)
                    break
                elif end_word == end_word[::-1]:
                    ans.append(1)
                    break
                else:
                    ans.append(2)
                    break
                    
                    
for i in ans:
    print(i)
    
    