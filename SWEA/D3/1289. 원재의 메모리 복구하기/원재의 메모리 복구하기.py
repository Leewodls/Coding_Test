
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a =input()
    count =0
    c_num='0'
    a = list(a)
    for i in a:
        if i != c_num:
            count+=1
            c_num=i
    print(f"#{test_case} {count}")         

    