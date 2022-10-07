
"""
표기식  + 스택활용 + 해결방법 찾기 

사실은 그냥 구현문제라고 봐도 무방.

가장 배운것 : 
배열에서 동시에 2개이상을 조작할때 직접삭제,삽입시 인덱스가 바뀌기떄문에 원하는 작업을 수행할수없음.

따라서 값을 내가 원하는 값으로 바꾼디 remove로 삭제하거나 또는 문자열같은경우에는 공백으로 지정후 연결해주는식으로

구현한다.

"""
import sys
input = sys.stdin.readline
import itertools

# 갯수는 괄호의 쌍 ! + 1
arr = str(input().rstrip())
temp = []
temp2 = []
temp3 = []
arr2 = list(arr)
answer = set()

for i in range(len(arr2)):
    
    if arr2[i] == '(':
        temp.append('(')
        temp2.append(i)
    elif arr2[i] == ')':
        
        temp.pop()
        k = temp2.pop()
        temp3.append([k,i])
temp3 = sorted(temp3)

for i in range(1,len(temp3)+1):
    for j in itertools.combinations(temp3,i):
        
        temp4 = list(arr)
        
        for k in j:
            st , end  = k
            temp4[st] = ''
            temp4[end] = ''
        
        answer.add(''.join(temp4))



for r in sorted(answer):
    print(r)

        