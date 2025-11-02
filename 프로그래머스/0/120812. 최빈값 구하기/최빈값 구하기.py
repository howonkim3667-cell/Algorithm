def solution(array):
    a = sorted(list(set(array)))
    b = {}

    if len(a) == 1:
        return a[0]
    for i in a:
        b[i] = array.count(i)

    a = [k for k, v in b.items() if max(b.values())== v]

    if len(a) >1:
        return -1
    return a[0]
    
# 딕셔너리에 담기