def solution(n):
    answer = []
    x = 2
    while x<=n:
        if not n%x:
            answer.append(x)
            n = n/x
        else:
            x+=1
    return sorted(set(answer))