def solution(arr, queries):
    temp = 0
    
    for idx, query in queries:
        temp = arr[idx]
        arr[idx]  = arr[query]
        arr[query] = temp
    return arr