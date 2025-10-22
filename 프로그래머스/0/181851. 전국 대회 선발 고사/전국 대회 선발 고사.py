def solution(rank, attendance):
    answer = {}
    for i in range(len(rank)):
        if attendance[i]:
            answer[rank[i]] = i
    d= sorted(answer.items())

    a, b, c = d[:3]
    return (10000*a[1])+(100*b[1])+c[1]
    