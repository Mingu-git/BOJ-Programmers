

import sys
input =sys.stdin.readline
from collections import deque


arr1 = str(input().rstrip())
arr2 = str(input().rstrip())

i = len(arr1)
j = len(arr2)
LCS = [ [0 for _ in range(i)] for _ in range(j)]


for i in range(i):
    for j in range(j):
        if i==0 or j==0:
            LCS[i][j] = 0
        elif arr1[i] == arr2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
 
print(LCS)