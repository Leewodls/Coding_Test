def solution(n):
    my_n = list(str(n))
    sum=0
    for i in range(len(my_n)):
        sum += int(my_n[i])
    
    return sum