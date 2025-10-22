def solution(my_string, queries):
    my_string = list(my_string)
    for start, end in queries:
        a= list(reversed(my_string[start:end+1]))
        my_string[start:end+1] = a
    return ''.join(my_string)
