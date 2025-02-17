def solution(myString, pat):
    
    mys = myString.replace('B','C').replace('A','B').replace('C','A')
    if pat in mys:
        return 1
    else:
        return 0
    