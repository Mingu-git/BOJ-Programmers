"""
염색체

문제 분석


배울점 정규 표현식

? : 0 or 1
+ : 1회 이상 반복
\n : 끝맷음
{s , e} 반복

match : 매치될시 문자열 반환 아니면 None 반환

findall :매치되는 것들 반환

"""

import sys
import re
input =sys.stdin.readline


temp = re.compile('[A-F]?[A]+[F]+[C]+[A-F]?\n')


N = int(input())

for i in range(N):
    
    if temp.match(input()):
        print("Infected!")
    else:
        print("Good")