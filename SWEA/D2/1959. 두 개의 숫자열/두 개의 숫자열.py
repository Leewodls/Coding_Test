T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a_num=0
	b_num = 0
	max_num = 0
	if n > m:
		for x in range(n-m+1):
			sum=0
			for i in range(m):
				sum+= a[i+x]*b[i]
			max_num = max(max_num, sum)
		print(f"#{test_case} {max_num}")

	elif n < m:
		for x in range(m-n+1):
			sum=0
			for i in range(n):
				sum += a[i] * b[i+x]
			max_num=max(max_num, sum)
		print(f"#{test_case} {max_num}")
        
	else:
		sum=0	
		for i in range(n):
			sum+= a[i]*b[i]
		print(f"#{test_case} {sum}")
        
            