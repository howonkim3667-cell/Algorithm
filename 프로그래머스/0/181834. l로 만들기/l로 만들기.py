def solution(myString):
    a = ''
    for i in myString:
        if i<'l':
            a+='l'
        else:
            a+= i
    return a