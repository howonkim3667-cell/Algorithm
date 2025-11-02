def solution(array):
    a = sorted(list(set(array)))
    b = {}
    print(a)
    if len(a) == 1:
        return a[0]
    for i in a:
        b[i] = array.count(i)
    print(b)
    a = [k for k, v in b.items() if max(b.values())== v]
    print(a)
    if len(a) >1:
        return -1
    return a[0]
    
# 딕셔너리에 담기