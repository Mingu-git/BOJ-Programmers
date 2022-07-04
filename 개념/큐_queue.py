"""
큐 _ queue 자료 구조


정리 
1. 우선순위 큐는 사실 쓸이유가 없다 -> 어차피 heapq 기준이고 오히려 더 느리다.

2. push,pop 자주 = deque
   인덱스활용한 data접근 = list

우선순위큐 : Thread-Safe / heapq  : Thread-Non-Safe -> 더빠름 안전한것을 확인하는것은 더 오래걸림.
"""



1. "우선순위 큐" (priority queue) : FIFO 구조, 삽입 상관 x But 제거시 사장 작은값을 먼저 제거.
"우선순위큐 : Thread-Safe / heapq  : Thread-Non-Safe -> 더빠름 안전한것을 확인하는것은 더 오래걸림." -> 10~30배

깊게 보면 heapq로 구현되어 있음. -> 루트 = 최소값 // 입력시 

from queue import PriorityQueue
"선언" : arr = PriorityQueue()

"추가" :arr.put(1) put을 이용하여 추가

"삭제" : arr.get() ->작은 값부터 리턴

"임의의 기준" : 1.튜플 형태 (순위,값) 저장 2.순위대로 값 get
arr.put((3,"민욱"))
arr.put((1,"유경"))
arr.get()[1] ->유경이 먼저 출력    
    
추가,삭제 모두 O(log N) 시간 복잡도를 가진다.





2. queue 큐  

2.1 "구현 방식 list" 

이때 삽입 => arr.insert(0,3) => 앞쪽에 삽입가능 뒤쪽은 arr.push()이용
-> 성능적으로 매우 안좋음 -> pop,insert -> O(N)
-> 주로 무작위 접근(random access)에 특화

2.2 "deque 이용"  : double ended queue 데이터를 양방향에서 추가 + 제거 가능

from collections import deque
arr = deque([1,2,3])
-> popleft ,appendleft  -> O(1)  = 시간복잡도 유리 
->but  무작위 접근에 -> O(N) ->why ? 내부적으로는 linked list 구조이기 때문 = i번째 i번 순회해야함


+@ arr.rotate(1 or -1 ) = 1 2 3 4 -> 4 1 2 3  // 4 1 2 3 -> 1 2 3 4