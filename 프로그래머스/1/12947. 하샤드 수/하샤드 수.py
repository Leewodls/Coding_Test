def solution(x):
    sum=0
    l = list(str(x))
    for i in l:
        sum +=int(i)
    if x%sum==0:
        return True
    else: return  False