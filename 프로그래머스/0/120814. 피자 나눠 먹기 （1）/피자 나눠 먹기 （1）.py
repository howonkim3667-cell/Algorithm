def solution(n):
    if n <=7:
        return 1
    else:
        a, b = divmod(n,7)
        if not b ==0:
            return a+1
        return a
    
    return answer