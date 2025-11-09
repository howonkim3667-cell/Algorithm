def solution(board):
    a = []
    len_ = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1,  1, -1,-1, 1]
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == 1:
                a.append([i,j])
    for x, y in a:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len_ and 0<= ny < len_:
                board[nx][ny] = 1
    count=0
    for i in board:
        for j in i:
            if j ==0:
                count+=1
    return count