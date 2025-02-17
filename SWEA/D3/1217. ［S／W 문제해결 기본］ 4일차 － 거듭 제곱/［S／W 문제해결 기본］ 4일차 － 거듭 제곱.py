T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    n, m = map(int, input().split())
    total=1
    for i in range(m):
        total = total*n
    print(f"#{tc} {total}")