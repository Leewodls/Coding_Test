T = int(input())
y=0
m = 0
d = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	a = int(input())
	y = a//10000
	m = (a%10000)//100
	d = (a%100)//1
	
	if y>0 and m>0 and m<13 :
		if m == 2:
			if d >0 and d<29:
				print(f"#{test_case} {y:04}/{m:02}/{d:02}")
			else : print(f"#{test_case} -1")
		elif m ==9 or m==11 or m== 4 or m==6:
			if d >0 and d<30:
				print(f"#{test_case} {y:04}/{m:02}/{d:02}")
			else: print(f"#{test_case} -1")
		elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			if d >0 and d<31:
				print(f"#{test_case} {y:04}/{m:02}/{d:02}")
			else: print(f"#{test_case} -1")
	else: 
		print(f"#{test_case} -1")