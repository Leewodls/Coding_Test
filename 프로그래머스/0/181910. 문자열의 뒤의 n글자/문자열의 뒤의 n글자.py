def solution(my_string, n):
    answer = my_string[-1:-n-1:-1]
    
    return answer[::-1]

# 문자열 my_string, 정수 n 