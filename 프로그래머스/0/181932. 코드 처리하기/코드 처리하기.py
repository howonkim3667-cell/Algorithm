def solution(code):
    answer = ''
    
    mode = 0
    for i in range(len(code)):
        if mode ==0:
            if not i%2 and not code[i] == '1':
                answer +=code[i]
            elif code[i] == '1':
                mode = 1
        elif mode ==1:
            if i%2 and not code[i] == '1':
                answer +=code[i]
            elif code[i] == '1':
                mode = 0
    if len(answer) == 0:
        return "EMPTY"
    
    return answer