def solution(n):
    a = 1
    for i in range(1,11):
        a*=i
        if a > n:
            return i-1
        if a == n:
            return i