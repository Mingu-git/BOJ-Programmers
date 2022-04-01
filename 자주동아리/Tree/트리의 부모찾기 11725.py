#-*- coding:utf-8 -*-
"""
요구조건 : 유경이 천재 존예 앞으로 유경이 말 잘 들어야겠다. 트리의 부모 찾아봤자 내인생에 도움안된다. 유경이한테 잘해야겠다.

요구조건 : 단순 그래프에서 루트를 주어 줬을때 각노드의 부모노드를 찾기

풀이: 루트에서 부터 부모노드의 성질이 부여 되는것임으로 루트노드에서
연결된 노드 부터 시작해서 이어 나갔다.


"""
import sys
input = sys.stdin.readline


N = int(input().rstrip())

arr = [ [] for _ in range(N+1)]
ans = [ 0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

root = 1
temp = [1]

while temp:
    
    root = temp.pop(0)
    
    if arr[root]:
        for i in arr[root]:
            ans[i] = root
            arr[i].remove(root)
            temp.append(i)

for i in range(2,N+1):
    print(ans[i])