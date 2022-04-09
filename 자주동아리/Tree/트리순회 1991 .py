#-*- coding:utf-8 -*-
"""
요구조건 : 이진 트리 구현 with 입력
1. class + 딕셔너리

2. 2차원배열로 구현

전위 , 중위 ,후위
print문의 순서 


"""

import sys
input = sys.stdin.readline

class Node:
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

def preorder(node):
  print(node.item)
  if node.left != '.':
    preorder(tree[node.left])
  if node.right != '.':
    preorder(tree[node.right])

def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])
  print(node.item)
  if node.right != '.':
    inorder(tree[node.right])

def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])
  print(node.item)
  
n = int(input().rstrip())
tree = {}

for _ in range(n):
  node, left, right = map(str, input().split())
  tree[node] = Node(item=node, left=left, right=right)

print(tree['A'].left)