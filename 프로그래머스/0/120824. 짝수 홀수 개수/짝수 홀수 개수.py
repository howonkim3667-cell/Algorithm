def solution(num_list):
    answer = []
    a = 0
    b = 0
    for i in num_list:
        if i%2:
            b+=1
        elif not i%2:
            a+=1
    return [a,b]