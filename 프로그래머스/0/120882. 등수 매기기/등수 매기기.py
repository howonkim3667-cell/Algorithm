# def mean(a):
#     return (a[0]+a[1])/len(a)

# def solution(score):
#     for i in range(len(score)):
#         score[i] = mean(score[i])
        
#     s_score = sorted(score, reverse = True)
    
#     answer = []
#     for i in score:
#         answer.append(s_score.index(i)+1)
#     return answer

def solution(score):
    mean_score = [sum(i)/len(i)for i in score]
    s_score = sorted([sum(i)/len(i)for i in score], reverse =True)
    
    
    print(s_score)
    dict = {}
    for i, v in enumerate(s_score):
        if v not in dict.keys():
            dict[v] = i+1
    print(dict)
    return [dict[i] for i in mean_score]