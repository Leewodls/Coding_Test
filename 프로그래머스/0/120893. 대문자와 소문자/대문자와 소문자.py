def solution(my_string):
    answer = ''.join(c.lower() if c.isupper() else c.upper() for c in my_string)
    return answer




