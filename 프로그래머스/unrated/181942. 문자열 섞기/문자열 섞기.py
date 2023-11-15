def solution(str1, str2):
    answer = ''
    
    str1_list = list(str1)
    str2_list = list(str2)
    
    num = 0
    
    for a in str1_list : 
        answer = answer + a
        answer = answer + str2_list[num]
        num = num + 1
    
    return answer