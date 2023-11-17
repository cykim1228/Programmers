def solution(a, d, included):
    answer = 0
    
    for i in included : 
        if i == True : 
            answer = answer + a
            a = a + d
        elif i == False : 
            answer = answer
            a = a + d
    
    return answer