a = int(input())
b = 0
sum = 0
while a>0:
    b = a%10
    sum += b
    a = a//10
print(sum)
    