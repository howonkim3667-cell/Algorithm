def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer+=[arr[i]]
        elif not len(answer) == 0 and answer[-1]== arr[i]:
            answer.pop()
        elif not len(answer) == 0 and not answer[-1]== arr[i]:
            answer+=[arr[i]]
        
    if len(answer)==0:
        return [-1]
    return answer