def solution(s):
    a = [i for i in s if s.count(i)==1]
    a.sort()
    return ''.join(a)