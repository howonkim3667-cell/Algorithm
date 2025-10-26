def solution(s):
    a= s.split()
    b = 0
    for i in range(len(a)):
        if a[i] =='Z':
            b -= int(a[i-1])
        else:
            b +=int(a[i])
        print(b)
        
    return b