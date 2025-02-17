T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    a=[]
    for i in range(100):
        b=list(map(int, input().split()))
        a.append(b)
    max_sum=0
    for i in range(100):
        sum2 =0
        sum1 =0
        for j in range(100):
            sum2 +=a[i][j]
            sum1 +=a[j][i]
        max_sum = max(max_sum, sum2, sum1)
    sum3=0
    for i in range(100):
        sum3 += a[i][i]
    max_sum = max(max_sum, sum3)
    sum4 =0 
    num=0
    for x in range(99, -1, -1):
        sum4 +=a[x][num]
        num+=1
    max_sum = max(max_sum, sum4)
    print(f"#{test_case} {max_sum}")