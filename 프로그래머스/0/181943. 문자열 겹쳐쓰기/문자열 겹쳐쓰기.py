def solution(my_string, overwrite_string, s):
    front = my_string[:s]
    back = my_string[len(overwrite_string)+s::]
    
    return front + overwrite_string + back
    