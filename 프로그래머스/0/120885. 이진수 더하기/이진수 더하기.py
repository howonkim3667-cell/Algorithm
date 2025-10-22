def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    c =bin(a+b)
    c= c.replace('0b', "")
    return c