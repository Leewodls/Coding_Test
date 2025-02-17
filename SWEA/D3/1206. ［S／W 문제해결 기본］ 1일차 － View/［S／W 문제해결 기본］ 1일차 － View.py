T = 10
for test_case in range(1, T + 1):
	n = int(input())
	a = list(map(int, input().split()))
	h=0
	sum=0
	for i in range(2, n-2):
		if a[i] > a[i-1] and a[i] > a[i-2] and a[i] > a[i+1] and a[i] > a[i+2]:
			h = a[i] - max(a[i-2], a[i-1], a[i+1], a[i+2])
			sum+=h
	print(f"#{test_case} {sum}")