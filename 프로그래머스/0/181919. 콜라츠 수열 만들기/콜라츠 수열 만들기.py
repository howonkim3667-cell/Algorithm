# for num in range(10,)

def solution(n):
    answer=[n]
    while n>1 :
        if not n%2:
            n//=2
        else:
            n = 3*n+1
        answer.append(n)
        
    return answer
print(solution(10))