#-*- coding:utf-8 -*-

import sys
input = sys.stdin.readline

"""
포인트는 : key - value 값을 활용해서 풀이 -> dic 시간복잡도

해쉬가 빠른건 a in dict  이게 빠름 + pop(list) == delete(dict)
pop 할때 순서지정시 시간복잡도 증가.
"""
def solution(phone_book):
    answer = True
    arr =  {}
    for i in phone_book:
        arr[i] = 0
    # 포인트는  접두사부터 검사한다는것 -> 따라서 하나부터 비교해서 길이를 비교 따라서 nxn의 시간복잡도가형성되는데 슬라이싱  
    
    # i = 비교대상 j 를 전체대상이라고 했을때
    # combination 은 어떤가???  만약에 전체를 다비교한다면..?
    
    
    #웬만하면 직접다 비교를 할 이유가 없음,,,[n^n 시간복잡도 최악 ]
    # 따라서 다돌려본다는건 꽤 좋은 방법이 아님
    # 숫자를 다루거나 비교할때는  정렬 = 비교이 효율적으로 될수도있음.
    # 딕셔너리의 정렬은 ?
    """풀이 1 :for 문 2개  + pop + slice 
    
    for i in phone_book:        
        for j in arr.keys():
            # 일단 다 돌려본다는게 
            if  len(str(j)) > len(str(i)):
                if j[:len(str(i))] == i:                    
                    answer = False          
            if not answer :
                break
        arr.pop(j)
             
        if not answer:
            break
    """
    """
    #풀이2: for 문 2개 +  in 2개
    
    # 문제는  선형탐색 ( 2중 반복문으로는 접근할수있지만)
    # 해쉬 값으로는 생각보다 접근하기가 어려웠다.
    for i in arr:
        temp = ""
        for j in i:
            temp += j
            print(i,j,temp)
            if temp in arr and temp != i: # dict in = O(1)
                answer = False
    """
    

# 정렬시 그전의 숫자에서 같지 않았던것은 그이후에 접두사가 같을 수없다.
# 그림으로 한번그려서 이해해 보자.
# 또한 길이가 다를경우 더긴길이의 부분은 자동으로 삭제된다.

"""풀이3 for 문 1개 + in 


    phone_book  = sorted(phone_book)
    for p1 , p2 in zip(phone_book,phone_book[1:]):
        print(p1,p2)
"""
    return answer


phone = ["119", "97674223", "1195524421","117"]

print(solution(phone))


