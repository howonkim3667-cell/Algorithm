def solution(arr, queries):
    answer = []
    for idx1, idx2, key_ in queries:
        current = [ i for i in arr[idx1:idx2+1] if i>key_]
        if len(current)==0:
            answer.append(-1)
        else: 
            answer.append(min(current))
        
    return answer