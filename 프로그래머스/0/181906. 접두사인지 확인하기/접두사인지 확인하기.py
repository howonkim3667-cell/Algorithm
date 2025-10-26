def solution(my_string,is_suffix):
    return int(is_suffix in [my_string[:i+1] for i in range(len(my_string))])
    
    