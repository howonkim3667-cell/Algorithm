def solution(num_list):
    a = 1
    if len(num_list) >10:
        return sum(num_list)
    else:
        for i in num_list:
            a *=i   
    return a