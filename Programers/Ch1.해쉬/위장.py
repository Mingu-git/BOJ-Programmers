#-*- coding:utf-8 -*-

import sys
input = sys.stdin.readline


"""
포인트 : 각 하나씩을 한다는게 목적

"""

def solution(clothes):
    answer = 0
    clothes_comb = {}
    
    
    for i in clothes:
        clothes_comb[i[0]] = i[1]
    
    
    
    
    
    
    
    
    
    return answer

arr = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(arr))