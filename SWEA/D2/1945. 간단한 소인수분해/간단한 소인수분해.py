T = int(input())

for test_case in range(1, T + 1):
	a = int(input())
	l = [0, 0, 0, 0, 0]
	while a>1:
		if a%2==0:
			l[0]+=1
			a = a//2
		elif a%3==0:
			l[1]+=1
			a = a//3
		elif a%5==0:
			l[2]+=1
			a = a//5
		elif a%7==0:
			l[3]+=1
			a = a//7
		elif a%11==0:
			l[4]+=1
			a = a//11
	print(f"#{test_case} {l[0]} {l[1]} {l[2]} {l[3]} {l[4]}")
    