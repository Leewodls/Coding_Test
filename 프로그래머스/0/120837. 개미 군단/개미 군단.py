def solution(hp):
    a = hp//5
    hp1 = hp%5
    b = hp1//3
    hp2 = hp1%3
    c = hp2//1
    answer = a+b+c
    return answer