"""
구현에 대한 공부

2023.05.13 update ver

1. combinaition , permutation

2. enumerate , zip

3. global , nonlocal

4. 백트랙킹

완전탐색 : 

브루트포스
비트마스크
재귀함수
순열
BFS,DFS
"""
from itertools import combinations, permutations




1. combinations , permutations

    목적 : 모든 경우의 수 탐색
        
    사용법 : 




2.구현 with enumerate , zip

    목적 :
        
    사용법 : 



3. global , nonlocal

    global (cf. 배열의 경우 주소값을 불러서 호출하기때문에 내부함수에서 불러도 바뀜)
    목적 : 함수 밖에 있는 전역변수를 함수내에서 변경할 수 있도록 해줌
    사용법 : 
    cnt =  100
    def logic():
        global cnt  # global 함수를 통해 전역변수인 cnt를 변경 
        cnt = 222
    logic()
    print(cnt) ==> 222 출력 

    nonlocal
    목적 : 내장 함수 내에서 구현할때 그 밖에 있는 함수에 있는 변수를 변경하기 위함
    주로 프로그래머스 코테대상
    사용법 : 
    def solution(num ,arr):
        
        ans = 0
        
        def dfs(x,y):
            nonlocal ans # 이렇게 해줘야  함수 밖에 있는 ans 값을 건드림
            if x == 1:
                ans += 1

        return ans
    

4. 백 트랙킹 (dfs와 교집함 이라고 생각을함)

    목적 : 모든경우의수를 탐색하다가 내가 설정한 조건에 부합하지 않을 경우에 다시
    돌아가는것은 백트랙킹이라고함 








1. find vs index  // 
a.find('x',1,3)
a.index('x',1,6) 변수 ,st,end
find : 문자열에서만 사용가능 없을시 -1 반환 
index : 없을경우 error발생 // dict 사용 x


1. 최소직사각형

풀이방법 : 만족하는 최소 직사각형 찾는게 문제의 핵심 (이때 가로,세로 회전가능)
따라서 세로,가로중 긴것은 긴것끼리 ,작은것은 작은것 끼리 하여 = 회전의 변수를 대처할 수 있었음

활용 : 어떠한 2 값을 바꿔서 최소값 추출시 -> 큰값은 큰값끼리 작은값은 작은 값 끼리 set헤서 풀이 가능

2.enumerate , combinations , permutations ,zip

"enumerate" : 인덱스와 함께 루프를 돌리고 싶다면..?
ex) for idx , k in enumerate(arr,start =??):
ex2)    for r,row in enumerate(coluumn):
            for c , letter in enumerate(row):
                print(r,c,letter)    // 2차원 배열 각 행과 문자 출력
                
"permutations" : 순열 , n 개중 r 골라 , 중복 X // import itertools
arr = list(itertools.permutations(arr,몇개))
for i in range(2,len(arr)+1):
        for k in list(permutations(arr,i)):
            num_temp = ""
            for j in k:
                num_temp += j

"zip" :동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어 반환
arr = zip([1,2,3],['A',"B","C"])


3. 완탐시 경우의수를 잘줄이기 위해서는 st,end 그리고 생략할 수 있는 조건 파악 중요

4. 방정식 구조
def fun(a,b,c):
    D=b*b-4*a*c
    if D>0:
        x1=round((-b-D**0.5)/2*a)
        x2=round((-b+D**0.5)/2*a)
        return (x1,x2)
    elif D==0:
        x=round(-b/2*a)
        return (x)
    else:
        return(0)

