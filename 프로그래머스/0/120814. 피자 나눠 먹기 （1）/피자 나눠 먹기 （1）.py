def solution(n):
    for i in range(50):
        if (7*i) < n:
            continue
        else:
            answer = i
            break
    return answer
