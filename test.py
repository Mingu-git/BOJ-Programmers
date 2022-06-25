import sys
input = sys.stdin.readline


class Node:
    def __init__(self,data):
        self.left = -1
        self.right =  -1
        self.data = data
        
tree = {}
ans = 0

phone = ["119", "97674223", "1195524421","117"]

arr = [[1,100],[2,123123],[3123,123]]

a = sorted(arr , key = lambda x : x[1])

for i in range(1, n):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
        
        
print(len(heap))



        