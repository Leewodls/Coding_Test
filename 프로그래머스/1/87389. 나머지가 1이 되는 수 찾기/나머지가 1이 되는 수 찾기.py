def solution(n):
    my_li=[]
    for i in range(1,n):
        if n%i==1:
            my_li.append(i)
    return min(my_li)