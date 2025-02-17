def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        a = numLog[i] - numLog[i-1]
        if i==0:
            continue
        if a == 10:
              answer+='d'
        elif a==-10:
              answer+='a'
        elif a==1:
              answer+='w'
        elif a==-1:
              answer+='s'
        
    
    return answer