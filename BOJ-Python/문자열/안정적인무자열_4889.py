import sys
input = sys.stdin.readline

from collections import deque
num = 1
ans = 0

while 1:
    
    
    txt = list(str(input().rstrip()))
    if txt[0] == '-':
        break
    
    
    print('%d. %d' %(num , ans ))
    
    # {} 맞춰지는것 뺴고 { / 2 끝 
    
    num += 1
    ans = 0
    
    