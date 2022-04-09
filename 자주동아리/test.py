import sys
input = sys.stdin.readline


class Node:
    def __init__(self,data):
        self.left = -1
        self.right =  -1
        self.data = data
        
tree = {}
ans = 0

N  = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
k  = int(input().rstrip())


        