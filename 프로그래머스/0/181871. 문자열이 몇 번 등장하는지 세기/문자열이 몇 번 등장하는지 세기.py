def solution(myString, pat):
    a = 0
    for i in range(len(myString)-len(pat)+1):
        print(myString[i:i+len(pat)])
        if pat == myString[i:i+len(pat)]:
            a +=1
    return a