
def solution(arr):
    
    
    big = []
    small = []
    
    for a,b in arr:
        if a>b:
            big.append(a)
            small.append(b)
        else:
            small.append(a)
            big.append(b)
    
    return  (max(big)*max(small))