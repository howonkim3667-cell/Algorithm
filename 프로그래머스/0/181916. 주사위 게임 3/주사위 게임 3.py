def solution(a, b, c, d):
    
    dict ={}
    for i in [a, b, c, d]:
        if i not in dict.keys():
            dict[i] = 1
        elif i in dict.keys():
            dict[i] +=1

    print(dict, len(dict))
    
    if len(dict) == 1:
        return 1111 * a
    if len(dict) == 4:
        return min(dict)
    if 3 in dict.values():
        for k,v in dict.items():
            if v ==3:
                p = k
            else:
                q = k
        return (10*p+q)**2
    if len(dict) ==3:
        c = []
        for k,v in dict.items():
            if not v ==2:
                c.append(k)
        return c[0]*c[1]
    
    if len(dict) ==2:
        c = list(dict.keys())
        return (c[0] + c[1]) * abs(c[0] - c[1])
            
        