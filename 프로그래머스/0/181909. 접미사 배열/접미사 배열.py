def solution(my_string):
    a=[]
    for i in range(-1, -len(my_string)-1, -1):
        a.append(my_string[i:])
    return sorted(a)