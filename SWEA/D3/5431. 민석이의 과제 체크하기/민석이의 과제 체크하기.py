T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    a=[]
    for i in range(1, n+1):
        a.append(i)
    for j in number:
            if j in a:
                a.remove(j)
    print(f"#{test_case}", *a)
        
    