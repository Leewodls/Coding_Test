T = int(input())

for test_case in range(1, T + 1):
    n = list(map(int,input().split()))
    max_n = max(n)
    min_n = min(n)
    n.remove(max_n)
    n.remove(min_n)

    result = round(sum(n)/len(n))
    print(f"#{test_case} {result}")