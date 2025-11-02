def solution(common):
    a = common[1] - common[0] 
    b = common[2] - common[1]
     
    if a == b:
        return common[-1] + b
    elif common[1] == 0:
        return 0
    else:
        c = common[-1]//common[-2]
        return int(common[-1]*c)
    
    
    
    # return answer