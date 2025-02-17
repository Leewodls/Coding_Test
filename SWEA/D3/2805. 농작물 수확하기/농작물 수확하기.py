T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a=[]
    m = n//2
    for i in range(n):
        b = list(map(int, input()))
        a.append(b)
    total =sum(a[m])
    for i in range(m):
        total += sum(a[i][m - i:m + i + 1])  
        total += sum(a[n - i - 1][m - i:m + i + 1])  
    print(f"#{test_case} {total}")

