def solution(emergency):
    a = emergency.copy()
    a.sort(reverse=True)
    c =[0]*len(a)
    for i in range(len(a)):
        b = emergency.index(a[i])
        c[b] = i+1
    return c