def solution(sides):
    a, b = sides
    diff = abs(a-b)
    sum_  = a + b
    print(diff, sum_)
    answer = [ i for i in range(diff+1, sum_)]
    
    return len(answer)