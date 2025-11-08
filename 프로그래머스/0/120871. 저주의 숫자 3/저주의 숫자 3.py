def solution(n):
    a = 0
    for i in range(1,n+1):
        while not a%3 or '3' in str(a):
            a+=1
        a+=1
        print(f'a : {a} i {i}')
    return a-1