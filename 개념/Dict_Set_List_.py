






1. DICT

2.dict로 정렬

-DefaultDict

from collections import defaultdict

arr = defaultdict("민욱")

기본값 설정가능 // key값 없을시 자연스럽게 기본값으로 value 설정



-sorted()

dict = sorted(dict.items() , reverse=True) #  key기준

# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(sorted(dic.items(), key=lambda x:x[1]))
# 위 값을 딕셔너리로 변환
print(dict(sorted(dic.items(), key=lambda x:x[1])))
# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))


3. 2차원 배열

from collection import defauldict

arr = defaultdict(list)

2차원 배열과 같음 사실상