T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    max_num = a[0]
    for i in range(1, len(a)):
    	if a[i]>max_num:
        	max_num = a[i]
    print(f"#{test_case} {max_num}")