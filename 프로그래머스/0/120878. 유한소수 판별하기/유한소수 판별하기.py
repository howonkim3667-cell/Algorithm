def solution(a, b):
    if a==b:
        return 1
    # 두 수의 최대공약수
    numer, denom = a, b
    while b !=0:
        temp = a
        a = b
        b = temp % b
    denom = denom//a
    print(denom)
    x = 2
    # 소인수
    answer= []
    while x<=denom:
        if not denom%x:
            answer.append(x)
            denom = denom/x
        else:
            x+=1
    
    answer = list(set(answer))
    if 2 in answer:
        v = answer.index(2)
        answer.pop(v)
    if 5 in answer:
        n = answer.index(5)
        answer.pop(n)
    if len(answer)== 0:
        return 1
    else:
        return 2