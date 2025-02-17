a, b = map(int, input().split())  
c = a - b 
for i in range(1, 999):
    b += i  
    if a == b:  
        break
print(c+1)
     