def solution(num_list):
    answer = 0
    plus = 0
    ultra = 1
    
    for i in num_list : 
        plus = plus + i
        ultra = ultra * i
    print(plus)
    print(ultra)
    
    if ultra < (plus * plus) : 
        answer = 1
    else : 
        answer = 0
    
    return answer