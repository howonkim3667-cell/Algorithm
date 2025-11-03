def solution(my_string):
    answer = ''
    a = 0
    for i in range(len(my_string)):
        if my_string[i].isnumeric():
            if my_string[i-1].isnumeric():
                answer+= my_string[i]
            else:
                answer+= " "+my_string[i]
    for i in answer.split():
        a+=int(i)
    return a

## 길이문제?