def solution(arr):
    a, b = len(arr), len(arr[0])
    if a==b:
        return arr
    if a>b:
        for i in range(a):
            arr[i]+=[0]* (a-b)
    if a<b:
        for i in range(b-a):
            arr.append([0]*b)
    return arr
            