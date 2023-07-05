"""

문자열

목표 : 문자열의 자유로운 touch 및 알고리즘 구현에 쉽게 구현

주로 리스트 / 셋 / 정렬 /딕트 / strip , split

+ 정규식으로 다 되는 느낌

+ 주로 스택구조를 활용해서 문자열 분리를 해줌

크기 고정되어 있는 배열 구현시는 슬라이딩 활용하여 (예를들어
문자열 크기가 4로 되어 비교를 진행할때)
앞뒤로 줄여주면서 슬라이싱 해주면 시간복잡도 o(N)

시간복잡도 향상가능

"""

import imp
from collections import defaultdict


1. 항상 슬라이싱 부터 생각해보자  + 문자열 뒤집기

[1:-1] , [2:-5:2]  규칙성있는 것에 사용시 항상 규칙에 유의하면서 사용

문자열 뒤집기 1: [::-1]  2: word = i + word (앞에 넣어줌으로써 뒤집기 가능.)

+ 마지막에 넣는 문자열 그냥 넣어주면됨


2. rstrip ,strip,split

strip은 각 방향으로 strip매개변수에 들어온 모든것을 제거 해줌
예를들어 adcba 라고 했을때

strip('acd')를 해주면 ba 가 됨



공백을 제거하기위해 사용할수도있지만 
"공백문자를 다른 문자로 치환 할때 에도 쓰임"

split : 문자열 분리시 이용



3. 문자열안에 무엇이 있는지 판단시

set + in 이 list + in 보다 빠르다

4. 연속성체크

a. 이전것과 비교 arr[j-1] ? arr[j]



5.정규표현식

import re

re.compile(~~~ 정규표현식 문자열 형태로) //예시  temp = re.compile('[A-F]?[A]+[F]+[C]+[A-F]?\n')

? : 0 or 1
+ : 1회 이상 반복
\n : 끝맷음
{s , e} 반복

match : 매치될시 문자열 반환 아니면 None 반환
findall :매치되는 것들 반환

6. 정렬

ㄱ.list로 정렬시 사전식 정렬


ㄴ.dict로 정렬

-DefaultDict

-sorted()

dict = sorted(dict.items() , reverse=True) #  key기준

# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(sorted(dic.items(), key=lambda x:x[1]))
# 위 값을 딕셔너리로 변환
print(dict(sorted(dic.items(), key=lambda x:x[1])))
# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))

ㄷ.2차원배열 or 문자의 갯수세기

from collection import defauldict

arr = defaultdict(list)

2차원 배열과 같음 사실상