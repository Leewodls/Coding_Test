T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    sum = 0
    n = int(input())
    for i in range(1, n+1, 2):
        sum+=i
    for j in range(0, n+1, 2):
        sum-=j
    print(f"#{test_case} {sum}")