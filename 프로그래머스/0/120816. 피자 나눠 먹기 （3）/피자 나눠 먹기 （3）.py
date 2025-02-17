def solution(slice, n):
    for i in range(100):
        if (slice*i) < n :
            continue
        else:
            answer=i
            break
    return answer

