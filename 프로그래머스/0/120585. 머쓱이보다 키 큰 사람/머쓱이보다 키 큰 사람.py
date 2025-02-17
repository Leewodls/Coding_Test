def solution(array, height):
    answer = 0
    for i in range(0,len(array), 1):
        if array[i] > height:
             answer+=1
        else:
            continue
    return answer