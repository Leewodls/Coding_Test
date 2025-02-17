T = int(input())

for test_case in range(1, T + 1):
    tc = int(input())
    b = [0]*101
    score = list(map(int, input().split()))
    max_num=0
    max_idx=0
    for i in range(len(score)):
        b[score[i]] += 1
    for j in range(101):
        if b[j] >= max_num:
            max_num = max(max_num, b[j])
            max_idx = j
    print(f"#{tc} {max_idx}")