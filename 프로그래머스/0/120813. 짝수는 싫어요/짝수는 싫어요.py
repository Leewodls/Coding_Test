def solution(n):
    answer = []
    
    for i in range(n+1):
        if i%2 == 0:
            continue
        else:
            answer.append(i)
    
    return answer

