def solution(x, n):
    answer = []
    if x>0:
        for j in range(x,x*n+1,x):
            answer.append(j)
    elif x<0 :
        for j in range(x,x*n-1,x):
            answer.append(j)
    else :
        answer = [0]*n
    return answer