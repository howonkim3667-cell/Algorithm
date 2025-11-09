def solution(numbers):
    answer = 0
    a = []
    for i in numbers:
        c = numbers.index(i)
        b = numbers.pop(c)
        print(numbers)
        for j in numbers:
            a.append(i*j)
        numbers.append(b)
    
    print(a)
    return max(a)