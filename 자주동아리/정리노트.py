#-*- coding:utf-8 -*-
#코드 내부에 한글데이터가 포함되있을경우 오류가 날때 위에 같이 utf-8설정을 직접해준다. 
#디버깅 설정을 바꿀수있지만 바꾸면 또 다른 세세한 에러나서 걍 이걸로 ㄲ

"""
이진트리 = 이진트리의 경우 left,right 성질이 있고 루트가
존제하기 때문에 self_init 으로 구현을 한다.

그래프 : 그래프는 루트가 없고 존제할수있는 경우의수가
비방향 그래프
방향그래프
가중치 그래프
이렇게 3가지가 있는데
한가지 방법중 하나는 인접리스트 형태로 구현하여 노드에서 갈수있는
모든 경우의수를 추가한다. // 중복될경우 list(set(arr))로 중복제거

더많은 공부 필요.
"""

1 binary 트리 자료 구조 구현
class Node:
    def __init__(self,data):  #init 함수는 객체가 생성될때마다 생성된다
        self.left = None
        self.right = None
        self.data = data

root = Node(10) #루트 노드 data = 10 저장
root.left = Node(88)  # 루트 오른쪽에   왼,오 내려갈수있는구조의 노드를 생성하게 해서 트리구조 구축

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
        
preorder(root)

# https://duwjdtn11.tistory.com/515
2 인접리스트
arr = [[]  for _ in range(N+1)]
for _ in range(M):
    a , b = map(int,input().rstrip().split()    arr[a].append(b)
    arr[b].append(a)