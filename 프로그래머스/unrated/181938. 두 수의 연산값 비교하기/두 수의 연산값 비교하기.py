def solution(a, b):
    answer = 0
    
    ab = str(a) + str(b)
    xab = 2 * a * b
    
    if int(ab) >= xab : 
        answer = int(ab)
    elif int(ab) < xab : 
        answer = xab
    
    return answer