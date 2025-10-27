def solution(arr, queries):
    answer = []
    for idx1, idx2 in queries:
        for i in range(idx1, idx2+1):
            arr[i] +=1
        
    return arr