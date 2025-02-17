T = 10

for test_case in range(1, T + 1):
    n = int(input())
    a = []
    sum_dead=0
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        s=0
        for j in range(n):
            if a[j][i] == 1:
                s =1
            if (a[j][i] == 2 and s==1):
                sum_dead+=1
                s=0
    print(f"#{test_case} {sum_dead}")
                
                
