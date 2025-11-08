def solution(n):
    answer = 0
    t = list(range(1, n+1))
    for i in t:
        count =0  
        d = list(range(1,i+1))
        for j in d:
            if not i%j:
                count +=1
        if count >= 3:
            answer +=1
    return answer
    