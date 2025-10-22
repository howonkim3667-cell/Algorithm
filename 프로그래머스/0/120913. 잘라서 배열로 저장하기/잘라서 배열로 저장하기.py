def solution(my_str, n):
    answer = []
    for i in my_str:
        answer.append(my_str[:n])
        my_str = my_str[n:]
        if not my_str:
            break
    return answer