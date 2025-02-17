T = int(input())
for test_case in range(1, T + 1):
    planet1 = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,"FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    planet2 = {0:"ZRO" , 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    tc, num = input().split()
    p = list(input().split())
    num = int(num)
    numbers = [planet1[i] for i in p]
    numbers.sort()
  
    numbers = [planet2[i] for i in numbers]
       
    print(f"{tc}", *numbers)
    
        