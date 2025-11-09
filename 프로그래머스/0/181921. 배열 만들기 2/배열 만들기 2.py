def solution(l, r):
    answer = []
    filter = ['0', '5']
    for i in range(l, r+1):
        state = True
        corr = str(i)
        for j in corr:
            if j not in filter:
                state = False
                break
        if state:
            answer.append(i)
    if len(answer) ==0 :
        return [-1]
    return answer



## 5 or 0만 들어있는 숫자
