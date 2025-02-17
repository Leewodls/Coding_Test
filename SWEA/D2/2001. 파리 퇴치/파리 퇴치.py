T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a =[]
    max_num=0
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            current_sum = 0  
            for x in range(m):
                for y in range(m):
                    current_sum += a[i + x][j + y]  
            max_num = max(max_num, current_sum)  
    print(f"#{test_case} {max_num}")  
            