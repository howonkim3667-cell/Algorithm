def solution(num_list, n):
    a=[]
    b=[]
    for i in range(10):
        if len(num_list)==0:
            return b
        a=[]
        for i in range(n):
            a.append(num_list[i])
        b.append(a)
        num_list=num_list[n:]
    return b
    