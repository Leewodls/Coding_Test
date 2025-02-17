def solution(box, n):
    
    for i in range(3):
        if i==0:
            a = box[i]//n
        elif i==1:
            b = box[i]//n
        elif i==2:
            c = box[i]//n
    return a*b*c