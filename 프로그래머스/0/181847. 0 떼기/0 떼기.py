def solution(n_str):
    
    for i, v in enumerate(n_str):
        if not v == '0':
            return n_str[i:]
        
    # return n_str.lstrip("0")