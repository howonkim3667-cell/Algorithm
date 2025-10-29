def solution(array):
    a=[]
    a.append(max(array))
    b = array.index(a[0])
    a.append(b)
    return [max(array), array.index(max(array))]