def solution(arr1, arr2):
    answer = 0
    sum1=0
    sum2=0
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else :
        for i in range(len(arr1)):
            sum1 += arr1[i]
            sum2 += arr2[i]
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        else : 
            return 0
    return answer