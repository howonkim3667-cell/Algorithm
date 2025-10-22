
def solution(arr, query):
    answer = arr
    for i, v in enumerate(query):
        if i%2:
            answer = answer[v:]
        elif not i%2:
            answer = answer[:v+1]
    return answer
