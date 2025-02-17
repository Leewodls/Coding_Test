def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n==0:
            answer.append(i)
    
    return answer

# 배열 numlist에서 n의 배수가 아닌 수 제거한 배열 리턴