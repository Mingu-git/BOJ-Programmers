"""
dic = {1:"zaaaaa" , 2:"ccccc"}

dict

dic = sorted(dic.items() ) #  key기준

# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(dic)


print(sorted(dic.items(), key=lambda x:x[1]))
# 위 값을 딕셔너리로 변환
#print(dict(sorted(dic.items(), key=lambda x:x[1])))
# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))
"""

import sys

a = False


temp = [[1,2]]

for x,y in temp:
    print(x,y)