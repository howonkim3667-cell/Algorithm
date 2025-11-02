def solution(keyinput, board):
    answer = [0,0]

    max_x = (board[0] - 1) // 2
    max_y = (board[1] - 1) // 2
    for i in keyinput:
        if i == "left":
            answer[0] -= 1
            if abs(answer[0]) > max_x:
                answer[0] += 1
        if i == "right":
            answer[0] += 1
            if abs(answer[0]) > max_x:
                answer[0] -= 1
        if i == "up":
            answer[1] += 1
            if abs(answer[1]) > max_y:
                answer[1] -= 1
        if i == "down":
            answer[1] -= 1
            if abs(answer[1]) > max_y:
                answer[1] += 1
        
    
    return answer