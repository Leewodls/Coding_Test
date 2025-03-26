def solution(x, n):
    answer = []
    sum = 0
    while n>0:
        sum+=x
        answer.append(sum)
        n-=1
    return answer