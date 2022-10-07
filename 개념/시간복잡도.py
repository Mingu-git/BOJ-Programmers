"""
시간복잡도 :
"""

1. 누적합

[12,3,4,6,7,8,9,10] M개의 길이의 구간합을 단순 for문으로 구현시
O(M)시간 형성 
N개의 구간 M 의 길 - > O(NM)

But 누적합을 이용하여 구간합을 구해보자.

누적합을 이용 = 누적합 계산 = Sj = O(M)
이때 N개의 구간에대해서 구하게 된다면
단순 누적합의 연산으로 구할수있기 때문에
시간복잡도는 O(M + N) 이 된다.

누적합 연산 = a[]의 i ~ j구간의 합은 S_j - S_i이다. 이런방식.


2. deque vs list

deque : push,pop(0) -> O(1) / arr[i] -> O(N)

list : push,pop(0),insert(0,123),delete(i) -> O(N) / arr[i],pop(),append() -> O(1) / sort  -> O(Nlog(N))

3. dict

검색, 삽입,삭제 -> O(1)

index , d[k] = v ,pop ,popitem() ,keys() -> O(1)
for k in d -> O(N)

+@ dict 구성

1. 기본적 선언

2. zip 활용

number = ['one','two'] , num = [1,2]

dict__ = dict(zip(number, num))
new_dict = {word : number for word , number in dict__.items() if numer > 1}  //for 문이용


4. reverse() ,rotate()

뒤지겁나 한칸씩 밀때는 다음과 같은것을 사용해보자
이때 reverse 매우 시간복잡도 크니 주의

이때 2번 뒤집을시 = 기본상태와 똑같기때문에
이런 기믹을 잘이해해보자.

5. in 연산을 할때에는 set으로 바꿔서 연산하기

for i in arr:
    print("!@#")

대신

for i in set(arr):
    print("!@#")
    
+@ 어떤 값이 있는 지찾을때는

setdefault("!@#" , "민욱")  //"!@#"이 있을 경우는 그 key값을 아닐 경우는 내이름을 반환!

시간복잡도 효율 상승



from collections import defaultdict  # 이것도 알아보자 .