def solution(my_string, is_prefix):
    answer=0
    if len(my_string) >= len(is_prefix):
        i = len(is_prefix)
        if my_string[0:i] == is_prefix[0:i]:
            answer = 1
        else : answer=0
    else : 
        answer=0
    
    return answer