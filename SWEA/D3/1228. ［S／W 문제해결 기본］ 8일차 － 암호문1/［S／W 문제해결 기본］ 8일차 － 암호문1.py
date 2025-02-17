T = 10

for test_case in range(1, T + 1):
    n = int(input())
    a = input().split()
    cmd_n = int(input())
    cmd = input().split('I')[1:]
    for i in range(cmd_n):
        arr = cmd[i].strip().split()
        x = int(arr[0])
        y = int(arr[1])
        for j in range(y):
            a.insert(x, arr[j+2])
            x+=1
    print(f"#{test_case}", *a[:10])  