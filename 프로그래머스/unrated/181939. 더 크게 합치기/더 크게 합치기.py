def solution(a, b):
    answer = 0
    
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    if ab >= ba : 
        answer = int(ab)
    elif ab < ba : 
        answer = int(ba)
    
    return answer