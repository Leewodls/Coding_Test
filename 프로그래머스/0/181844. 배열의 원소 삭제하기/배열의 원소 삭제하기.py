def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            idx = arr.index(i)
            arr.pop(idx)
    return arr