T = int(input())

for test_case in range(1, T + 1):
    time = list(map(int, input().split()))
    h=0
    m=0
    h = time[0] + time[2]
    m = time[1] + time[3]
    if h >12:
        h = h-12
    if m > 59:
        h +=1
        m-=60
    print(f"#{test_case} {h} {m}")