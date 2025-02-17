n = int(input())
a = list((str(i) for i in range(1, n+1)))
result = []
for i in range(len(a)):
    count = a[i].count('3') + a[i].count('6') + a[i].count('9')
    if count > 0:
        a[i] = '-' * count
        
for i in a:
    print(i, end=" ")