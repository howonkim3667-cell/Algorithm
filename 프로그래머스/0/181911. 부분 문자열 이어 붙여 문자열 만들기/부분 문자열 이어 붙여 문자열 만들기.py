def solution(my_strings, parts):
    answer = []
    for idx, value in enumerate(my_strings):
        s, n = parts[idx]
        answer.append(value[s:n+1])
    return ''.join(answer)