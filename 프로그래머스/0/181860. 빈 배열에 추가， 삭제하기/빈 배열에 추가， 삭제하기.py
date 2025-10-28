
def solution(arr, flag):
    answer = []
    for i, b in zip(arr, flag):
        if b:
            answer+= [i]*i*2
        else:
            answer = answer[:-i]
    return answer
            