#1 : nxn 배열
arr = [[] for _ in range(5)]

#2 해쉬
"""
해쉬는 언제 사용하면 좋을까?
1. 리스트를 쓸 수 없을 때  즉 dict 자료구조를 통해 해시 구현

2.빠른접근 / 탐색이 필요할때
-> 딕셔너리를 사용 -> O(1) 대부분 시간복잡도

3.집계가 필요
원소의 개수를 세는문제 - >collection + Counter

4.구조 
-> key - value  = >  'name' = '민욱' , 'age' = 14

5. 활용 함수 
    a. get : get(key,x) -> 없을때 x 리턴
    
    b. set,update : dict['~'] = 100
    
    c. Delete : del dict[key] , dict.pop(key,valie)
    
    d. Iterate    
        가.key로 순회
        for key in dict:
               
        나.key,value 동시 순회
        for key,value in dict.items():
            
    e. 조회 : print("key" in dict) ,dict.values(),items()
    
    f. 정렬 : 
        가 .key item 정렬시 :sorted(dic.items() , revereste = True)
        
        나 . value 기준 정렬시 : dic2 = sorted(dic.items(), key = lambda item : item[1]) 
            item[1] -> key 값을 기준으로 하는걸 설정
            key 기준 정렬시 item[0]으로 해주면됨
            
        다. age 내림차순후 name 으로 오름차순
            stu_sorted = sorted(student, key = lambda item : (-item['age'], item['name']))
        
        라  age 오름 차순후 name 내림 차순( sorted와itemgetter 이용)
            from operator import itemgetter
            stu_sorted = sorted(student, key = itemgetter('age','name'))
        
6.시간 복잡도: https://wiki.python.org/moin/TimeComplexity
순회,복사 빼고 대부분 1

"""