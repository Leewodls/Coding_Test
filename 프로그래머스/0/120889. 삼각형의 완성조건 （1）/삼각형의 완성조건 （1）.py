def solution(sides):
    a=0
    for i in sides: 
        a += i
    b= a-max(sides)
    if max(sides) >= b:
        answer = 2
    else:
        answer = 1
    return answer