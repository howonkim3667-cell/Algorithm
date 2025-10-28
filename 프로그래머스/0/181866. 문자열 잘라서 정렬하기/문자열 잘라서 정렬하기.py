def solution(myString):
    a = list(filter(None, myString.split("x")))
    a.sort()
    return a