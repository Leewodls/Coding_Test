def solution(my_string):
    answer = []
    for i in my_string:
        for x in range(10):
            if i == str(x):
                answer.append(int(i))
    answer = sorted(answer)
    return answer