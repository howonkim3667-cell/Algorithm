def solution(myString, pat):
    a = myString.replace('A', "*").replace('B', "A").replace('*', "B")
    return int(pat in a)