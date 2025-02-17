T = 10
for test_case in range(1, T + 1):
    n = int(input())
    a=[]
    for i in range(8):
        b = list(input().strip())
        a.append(b)
    num=0
    
    for i in range(8):
        for j in range(8-n+1):
            if a[i][j:j+n] == a[i][j:j+n][::-1]:  
                num += 1
    for i in range(8):
        for j in range(8-n+1):
            vertical = [a[x][i] for x in range(j, j+n)]  
            if vertical == vertical[::-1]:  
                num += 1
    print(f"#{test_case} {num}")        
            