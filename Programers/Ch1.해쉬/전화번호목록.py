import sys
input = sys.stdin.readline


def solution(phone_book):
    answer = True
    
    arr =  {}
    
    for i in phone_book:
        arr[i] = 0
    
    # 포인트는  접두사부터 검사한다는것 -> 따라서 하나부터 비교해서 길이를 비교 따라서 nxn의 시간복잡도가형성되는데 슬라이싱
    # i = 비교대상 j 를 전체대상이라고 했을때
    for i in phone_book:
        
        for j in arr.values():
            if i != j and len(str(j)) > len(str(i)):
                if j[:len(str(i))] == i:
                    
                    answer = False
            del arr[j]
            if not answer :
                break
            
        if not answer:
            break
                
   
    return answer




print(solution(["12","123","1235","567","88"]))

