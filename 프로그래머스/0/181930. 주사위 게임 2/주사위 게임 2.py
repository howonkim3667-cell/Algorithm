def solution(a, b, c):
    a=[a,b,c]
    max_ = max([a.count(i) for i in a])
    result = 1
    num=0
    for i in range(max_):
        for n in a:
            num += pow(n, i+1)
        result = result*num
        num=0
    return result