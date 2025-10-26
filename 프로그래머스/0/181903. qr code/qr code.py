def solution(q, r, code):
    a =''
    for i in range(len(code)):
        if i%q == r:
            a+=code[i]   
    return a