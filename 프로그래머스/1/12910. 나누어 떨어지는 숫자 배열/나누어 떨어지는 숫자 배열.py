def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor ==0:
            answer.append(arr[i])
    if len(answer) == 0: return [-1]
    answer = sorted(answer)
    return answer