T = int(input())

for test_case in range(1, T + 1):
	sum=0
	a = list(map(int, input().split()))
	for i in a:
		sum+=i
	print(f"#{test_case} {round(sum/10)}")
        