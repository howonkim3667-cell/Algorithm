def solution(my_string):
    data = []
    answer = list(range(65, 91))
    answer += list(range(97,123))
    result = []
    for i in my_string:
        data.append(ord(i))
    for i in answer:
        result.append(data.count(i))
    return result