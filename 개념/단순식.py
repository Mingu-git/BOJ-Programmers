""" 
단순식 모음

"""

1. 람다 :arr.sort(key = lambda x : x[1])  x[1] 대신 len(x)등 여러가지 가능.

2.arr = list(map(int,input().rstrip().split())) vs arr = (map(int,input().rstrip().split())) //vs코드상 결과 same 가끔
boj컴파일시 type error발생 list 붙여주자

3.f = sorted(e, key = lambda x : (x[0], -x[1])) 정렬시 1. 첫번째원소 오름차순 2. 두번째 원소 내림차순 정렬