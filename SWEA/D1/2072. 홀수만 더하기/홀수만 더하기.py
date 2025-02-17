
T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    total_sum = 0 
    
    for j in a:
        if j % 2 == 0:
            continue  
        else:
            total_sum += j  
    print(f"#{test_case} {total_sum}")

