"""
import sys
input = sys.stdin.readline

def solution(participant, completion):
    
    
    for i in completion:
        if i in participant:
            participant.remove(i)
            
    
    
    
    answer = participant
    return answer
    
"""
# dict 는 find , 삭제가 O(1)

def solution(participant, completion):
    
    arr = {}
    
    for i in participant:
        if i in arr:
            arr[i] = int(arr[i]) + 1
           
        else:
            arr[i] = 0
    
    for j in completion:
        if arr[j] != 0:
            arr[j] = int(arr[j])-1
        else:
            arr.pop(j)
        
    for key in arr:
        answer = key
    
    return answer


print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))