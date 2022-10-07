""" 
단순식 모음

"""

1. 람다 :arr.sort(key = lambda x : x[1])  x[1] 대신 len(x)등 여러가지 가능.

2.arr = list(map(int,input().rstrip().split())) vs arr = (map(int,input().rstrip().split())) //vs코드상 결과 same 가끔
boj컴파일시 type error발생 list 붙여주자

3.f = sorted(e, key = lambda x : (x[0], -x[1])) 정렬시 1. 첫번째원소 오름차순 2. 두번째 원소 내림차순 정렬

"""
팁모음

"""

1.상태변이 변수를 통한 if 문 제어시

상태변이 조건을 먼저따지는게 쉬움


2. 조건 문으로 하나씩 문자를나눌때 마지막에 분기조건을 못만족할때는

예를 들어 "ABC"를 할때  하나씩 문자를 temp 에 넣어준후 마지막 처리를할때는 len(arr)+1 가 없기때문에 조건문에 못들어간다
따라서 temp 에 들어간 그대로 넣어주면  완성.

그자체를 넣어주면된다.