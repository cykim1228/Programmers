def solution(n):
    answer = 0
    
    # n이 짝수
    if n % 2 == 0 : 
        for i in range(n+1) : 
            if i % 2 == 0 : 
                answer = answer + i * i
            else : 
                answer = answer
                
    # n이 홀수
    else : 
        for i in range(n+1) : 
            if i % 2 == 0 : 
                answer = answer
            else : 
                answer = answer + i
                # 1 0 3 0 5 0 7
    
    return answer