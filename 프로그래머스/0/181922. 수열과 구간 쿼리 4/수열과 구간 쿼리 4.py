def solution(arr, queries):
    for idx1, idx2, key_ in queries:
        for i in range(idx1, idx2+1):
            if not i%key_:
                arr[i] +=1
    return arr
