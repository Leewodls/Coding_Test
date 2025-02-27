def solution(n, k):
    answer=[]
    for i in range(1, n+1):
        if n%i==0:
            answer.append(i)
    if k > len(answer):
        return 0
    return answer[k-1]
        
n, k = map(int, input().split())
print(solution(n, k))