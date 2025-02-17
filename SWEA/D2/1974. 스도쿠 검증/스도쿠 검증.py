T = int(input())

for test_case in range(1, T + 1):
    result = 1
    a = []
    

    for i in range(9):
        b = list(map(int, input().split()))
        a.append(b)
    

    for i in range(9):
        row_check = set()
        col_check = set()
        for j in range(9):
            row_check.add(a[i][j])
            col_check.add(a[j][i])
        if len(row_check) != 9 or len(col_check) != 9:
            result = 0
            break


    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_check = set()
                for x in range(3):
                    for y in range(3):
                        square_check.add(a[i + x][j + y])
                if len(square_check) != 9:
                    result = 0
                    break
            if result == 0:
                break
    
    # 결과 출력
    print(f"#{test_case} {result}")