def solution(spell, dic):
    answer= []
    for i in dic:
        state = True
        for j in spell:
            if j not in i:
                state =False
                break
        if state:
            answer.append(i)
    if len(answer) == 0:
        return 2
    return 1
    
