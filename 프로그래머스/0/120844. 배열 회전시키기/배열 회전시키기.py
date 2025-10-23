def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers.pop(-1))
        answer+=numbers
        return answer
    elif direction == 'left':
        answer+=numbers[1:]
        answer.append(numbers.pop(0))
        return answer
