
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	p,q,r,s,w = map(int, input().split())
	a, b = 0, 0
	if w>r :
		a = (w - r) * s + q
	else : a = q
	b = p*w
	if a>b:
		print(f"#{test_case} {b}")
	else:         
		print(f"#{test_case} {a}")