def solution(arr):
    if len(arr) == 0:
        return arr        
    i = 1
    while True:
        if len(arr) <i:
            arr += [0]*abs((len(arr)-i))
            break
        elif len(arr) == i:
            break
        i*=2
    return arr
            