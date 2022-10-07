"""
2493 탑

스택 + heapq(최대 최소 )

얻어갈것 : 
1. 분기점 flag 로 구현가능. == 이것은 전체를 [0]으로 매핑하고 하나씩 바꾸는것과 비슷할수있다.
즉 분기점으로 구분해서하는구현 = 전체매핑해서 하는 구현

2.

"""
import sys
input =sys.stdin.readline

N = int(input().rstrip())
Twr = list(map(int , input().rstrip().split()))
st = [[Twr[0],1]]
ans = [0]

for i in range(1,N):
    temp = False
    while st:
        if st[-1][0] < Twr[i]:
            st.pop()
        else:
            ans.append(st[-1][1])
            st.append([Twr[i],i+1])
            temp = True
            break
    if not temp:
        st.append([Twr[i],i+1])
        ans.append(0)
            
print(*ans)


    
    