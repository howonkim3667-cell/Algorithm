def solution(arr):
    answer =[]
    if 2 not in arr:
        return [-1]
    for i in range(len(arr)):
        if arr[i]==2:
            answer.append(i)
    
    return arr[answer[0]:answer[-1]+1]

# 리스트의 해당 데이터의 인덱스 확인
# find or index
# 다음 인덱스 확인하려면?
# find, index 매개변수 확인 
