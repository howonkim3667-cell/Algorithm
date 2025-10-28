def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        a, b = sum(arr1), sum(arr2)
        if a<b :
            return -1
        if a>b:
            return 1
        if a==b:
            return 0
    elif len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1