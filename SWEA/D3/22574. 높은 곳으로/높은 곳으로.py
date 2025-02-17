T = int(input())

for test_case in range(1, T + 1):
    n, p = map(int, (input().split()))
    lay=0
    for i in range(1, n+1, 1):
        if lay + i ==p:
            if lay +i >1:
                lay= lay+i-1
            else:
                continue
        else :lay +=i
    print(lay)
        
        
