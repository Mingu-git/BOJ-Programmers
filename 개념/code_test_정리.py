#-*- coding:utf-8 -*-
#코드 내부에 한글데이터가 포함되있을경우 오류가 날때 위에 같이 utf-8설정을 직접해준다. 
#디버깅 설정을 바꿀수있지만 바꾸면 또 다른 세세한 에러나서 걍 이걸로 ㄲ
1.트리
2.그래프
3.해쉬


<tree 구조>

"""
이진트리 = 이진트리의 경우 left,right 성질이 있고 루트가
존제하기 때문에 self_init + 딕셔너리 or 2차원 배열 으로 구현을 한다.


그래프 : 그래프는 루트가 없고 존제할수있는 경우의수가
비방향 그래프
방향그래프
가중치 그래프
이렇게 3가지가 있는데
한가지 방법중 하나는 인접리스트 형태로 구현하여 노드에서 갈수있는
모든 경우의수를 추가한다. // 중복될경우 list(set(arr))로 중복제거

더많은 공부 필요.
"""

1.1binary 트리 자료 구조 구현
class Node:
    def __init__(self,data,left,right):  #init 함수는 객체가 생성될때마다 생성된다
        self.left = left
        self.right = right
        self.data = data
tree = {} # 딕셔너리와 함께 써줘야된다.
tree[node] = Node(data,left,right)
print(tree["A"]) # 이런식으로 구현
root = Node(10,2,3) #루트 노드 data = 10 저장
 # 루트 오른쪽에   왼,오 내려갈수있는구조의 노드를 생성하게 해서 트리구조 구축

1.2 이진 트리 2차원 배열 ( 리스트를이용)
s = [[0] * 3 for _ in range(26)]
item = ord(node) - 65
s[item][0], s[item][1], s[item][2] = node, left, right

이때에는 arr[ord(A) - 65]형태로 해줘야한다.
리스트를 쓸시에는 숫자로 순서를 매겨줘야 하기 때문이다.


# https://duwjdtn11.tistory.com/515
2 인접리스트
arr = [[]  for _ in range(N+1)]
for _ in range(M):
    a , b = map(int,input().rstrip().split()    arr[a].append(b)
    arr[b].append(a)
    
    
3.Trie  = 문자열을 저장하고 효율적으로 탐색하기 위한
트리형태의 자료 구조 
-> 전화 번호부 목록을 그렇게 풀수있음.

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 복습시 트리 1068 코드 부터보고 다시 해보기.

<Graph>

1. tree 와 graph 차이 : 
    Tree : 부모 -> 자식 노드로 내려가는 방향    ====>>>>>>>> 그래프의 한종류
    그래프 : 정점과 간선간의 구조   -> 양방향 ,단방향 , 가중치 

2. 그래프 표현의 종류 
    a . 인접행렬  matrix 를 통해 구현 O(N^2)  전체 메모리 큼 but 특정 값을찾는건 빠름
    
    b . 인접리스트 : O(V+E)  : 딕셔너리 형태로 구현  ex) graph = { 0 : [1,2,3]  , 1 : [2,4] } //시작노드는 Key 값으로 연결되어진 노드는 value 값으로 생성
    or 2차원 리스트구조로 구현 : ex) graph = [[1,2,3,] , [2,4] ] 
    
    
    
    

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 해쉬 .

<해쉬>

해쉬는 언제 사용하면 좋을까?
1. 리스트를 쓸 수 없을 때  즉 dict 자료구조를 통해 해시 구현

2.빠른접근 / 탐색이 필요할때
-> 딕셔너리를 사용 
-> list 보다 좋은점은? =  
ㄱ. a in dict = 1  && a in list = O(k)
ㄴ. pop() == delete // pop(k) = O(K)

3.집계가 필요
원소의 개수를 세는문제 - >collection + Counter

4.구조 
-> key - value  = >  'name' = '민욱' , 'age' = 14
이때 zip(a,b)를 활용하여 하면 편하게 비교 가능 이때
ex) for i ,j in zip(book , card):
    각각의 원소를 각각 불러와서 사용할수이음


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



    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 복습시 트리 1068 코드 부터보고 다시 해보기.

    
    
    