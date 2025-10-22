def solution(arr, k):
    a =[]
    for i in arr:
        if i not in a:
            a.append(i)
    
    if len(a)<k:
        for i in range(k-len(a)):
            a.append(-1)
        return a
    else:
        return a[:k]    

## 정렬되지 않은 무작위 수 앞에서 순서대로 추출, set, sort 사용 X