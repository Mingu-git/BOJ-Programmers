"""
1541

1. 일단 최소가 되도록 해야한다 ==> 약간 그리디 느낌 ( 최적값 도출 유도 )

2. 괄호를 친다는 의미..??

3. 일단 계싼 ==> 주로 스택을 활용하여 계산 진행

맥스 길이는 50
가지고 있는 연산자 - + 
입력 1 : - 가 있는 부분을 기준으로 최댓값이 있도록 구현

입력 2: - 가 없다면 그냥 그대로 더하여 return

-가 나타나면 -가 다시 나타날때까지 임시 스택에 더해주기
"""

import sys
input = sys.stdin.readline

temp = str(input().rstrip())
arr = ['+' , '-']

mul = set( arr )
stack = ''

stack_minus = 0
stack_plus = 0

flag = 0
num = 0

for i in range(len(temp)):
    if temp[i] not in mul:
        stack += temp[i]
        
        if i == len(temp)-1:
            num = int(stack)
            
            if flag == 1:
                stack_minus += num
            else:
                stack_plus += num
    else:
        
        if temp[i] == '-' and flag == 0:
            num = int(stack)
            stack = ''
            stack_plus += num
            flag = 1
        elif flag == 0:
            num = int(stack)
            stack = ''
            stack_plus += num
        
        elif flag == 1:
            num = int(stack)
            stack = ''
            stack_minus += num
        
    #print(stack_plus, stack_minus , stack)


ans = stack_plus - stack_minus

print(ans)
"""
for i in temp:
    if i not in mul:
        stack += i
    elif i in mul: # + 또는 - 가 나왔을 경우
        # 총 4가지 경우가 있다고 생각
        # 1. - 가 처음 나왔을때 ==> 다음 - 가 나올때까지 flag = 1 -> flag =0
        
        
        if i == '-'  :
            flag *= -1 # 괄호가 시작될때 1 / 괄호가 닫힐때 -1
        
        if flag == 1:
            num = int(stack)
            stack = ''
            stack_minus += num
        elif flag == -1:
"""

   
                  
        
        





