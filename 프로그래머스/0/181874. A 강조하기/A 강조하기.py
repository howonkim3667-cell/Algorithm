def solution(myString):
    a =''
    ['a', 'A']
    for i in myString:
        if i in ['a', 'A']:
            a+=i.upper()
        else:
            a+=i.lower()
    return a