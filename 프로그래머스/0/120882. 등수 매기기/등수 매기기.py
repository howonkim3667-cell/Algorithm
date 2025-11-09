def mean(a):
    return (a[0]+a[1])/len(a)
def solution(score):
    for i in range(len(score)):
        score[i] = mean(score[i])
        
    s_score = sorted(score, reverse = True)
    
    answer = []
    for i in score:
        answer.append(s_score.index(i)+1)
    return answer