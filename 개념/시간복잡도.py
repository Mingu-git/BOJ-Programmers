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
index , d[k] = v ,pop ,popitem() ,keys() -> O(1)
for k in d -> O(N)