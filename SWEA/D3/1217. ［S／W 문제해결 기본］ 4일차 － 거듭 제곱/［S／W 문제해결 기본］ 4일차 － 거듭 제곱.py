T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    n, m = map(int, input().split())
    result = 1
    for i in range(m):
        result = result*n
        
    print(f"#{tc} {result}")