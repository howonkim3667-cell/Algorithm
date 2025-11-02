def solution(my_string):
    a = []
    for i in my_string:
        if i.isnumeric():
            a.append(int(i))
    return sorted(a)
