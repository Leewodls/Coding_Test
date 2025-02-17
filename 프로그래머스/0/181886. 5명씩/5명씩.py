def solution(names):
    answer = []
    for i in names:
        if names.index(i)%5==0:
            answer.append(i)
    return answer