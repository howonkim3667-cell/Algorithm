def solution(hp):
    result = 0
    if hp==0:
        return 0
    # a, b = divmod(hp, 5)
    # if  b==0:
    #     result+=a
    #     return result
    # result+=a
    # c, d = divmod(b, 3)
    # if d ==0:
    #     result+=c
    #     return result
    # result+=c
    # e, f = divmod(c, 1)
    # if f ==0:
    #     result+=e
    #     return result
    
    a = [5, 3, 1]
    c = hp
    result = 0
    for i in a:
        b, c = divmod(c, i)
        result += b
        if c == 0:
            return result
    
    
