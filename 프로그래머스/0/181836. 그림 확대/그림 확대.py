def solution(picture, k):
    b = [] 

    for i in picture:
        a = ''
        for j in range(len(i)):
            a+= i[j]*k
        b+= [a]*k
    c = '\n'.join(b)
    return b