def solution(slice, n):
    a = slice
    while True:
        if int(slice//n) > 0:
            return slice/a
        else:
            slice += a
        
        
    
    