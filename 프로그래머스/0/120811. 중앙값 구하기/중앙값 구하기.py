def solution(array):
    array.sort()
    
    index=int(len(array)/2)
    
    answer = array[index]
    return answer