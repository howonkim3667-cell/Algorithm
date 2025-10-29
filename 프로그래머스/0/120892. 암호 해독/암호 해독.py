def solution(cipher, code):
    a=''
    idx = code-1
    while idx < len(cipher):
        
        a+=cipher[idx]
        idx+=code
        print(idx)
    return a