def solution(start_num, end_num):
    answer = []
    for i in range((end_num-start_num)+1):
        answer.append(start_num)
        start_num+=1
    return answer