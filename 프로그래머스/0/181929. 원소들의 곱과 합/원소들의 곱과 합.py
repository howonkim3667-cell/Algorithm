def solution(num_list):
    b=1
    for i in num_list:
        print(i)
        b *= i
    print(b)
    c=(sum(num_list))**2
    print(c)
    if b < c :
        return 1
    else:
        return 0