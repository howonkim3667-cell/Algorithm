def solution(i, j, k):
    a = list(range(i,j+1))
    b = [str(i) for i in a]
    c = ''.join(b)
    return c.count(str(k))
