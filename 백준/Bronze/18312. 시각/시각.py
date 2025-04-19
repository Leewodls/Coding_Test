
n, k = map(int, input().split())
count = 0
for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            if str(k) in f"{hour:02}{minute:02}{sec:02}":
                count+=1
print(count)
