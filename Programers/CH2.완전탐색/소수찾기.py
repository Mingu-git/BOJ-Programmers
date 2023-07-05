def solution(numbers):
    from itertools import permutations
    def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
        for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
            if x % i == 0 :
                return 0 # 소수가 아님
        if x == 1 or x == 0:
            return 0
        return 1 # 소수임
    
    ans= 0
    arr = []
    temp = []
    for i in numbers:
        arr.append(str(i))
        if i != "0":
            temp.append(int(i))
    # 모든 숫자 조합구하기
    
    
    for i in range(2,len(arr)+1):
        for k in list(permutations(arr,i)):
            num_temp = ""
            for j in k:
                num_temp += j
            
            if num_temp[0] == '0':
                num_temp = num_temp[1:]
                temp.append(int(num_temp))
            else:
                temp.append(int(num_temp))
    
    arr_num = sorted(list(set(temp)))            
    print(sorted(list(set(temp))))
    
    for i in arr_num:
        ans += is_prime_number(i)
                
            
    
    
    # 0앞에 있는거 때주고
    
    # 소수구별
    
    
    # 정답 출력
    
    return ans