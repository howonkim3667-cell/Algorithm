def solution(n):
    piece = 6
    count =1
    while True:
        if piece%n==0:
            return count
        count +=1
        piece += 6
        
        
#  6과 n의 최소공배수
