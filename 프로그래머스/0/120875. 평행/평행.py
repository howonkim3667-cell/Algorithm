# def solution(dots):
#     x1, y1 = dots[0]
#     x2, y2 = dots[1]
#     x3, y3 = dots[2]
#     x4, y4 = dots[3]
#     a = abs((y2-y1)/(x2-x1))
#     b = abs((y3-y2)/(x3-x2))
#     c = abs((y4-y3)/(x4-x3))
#     d = abs((y1-y4)/(x1-x4))
#     answer = [a,b,c,d]
    
#     if len(set(answer)) == len(answer):
#         return 0
#     else:
#         return 1

# def solution(dots):
#     x1, y1 = dots[0]
#     x2, y2 = dots[1]
#     x3, y3 = dots[2]
#     x4, y4 = dots[3]
#     if abs((y2-y1)/(x2-x1)) == abs((y3-y2)/(x3-x2)):
#         return 1
#     if abs((y3-y1)/(x3-x1)) ==  abs((y2-y4)/(x2-x4)):
#         return 1
#     if abs((y1-y4)/(x1-x4)) == abs((y3-y2)/(x3-x2)):
#         return 1
#     else:
#         return 0
#     b = 
#     c = abs((y4-y3)/(x4-x3))
#     d = abs((y1-y4)/(x1-x4))
#     answer = [a,b,c,d]
    
#     if len(set(answer)) == len(answer):
#         return 0
#     else:
#         return 1

def solution(dots):
    a, b, c, d = dots
    if abs((a[0]-b[0]) / (a[1]-b[1])) == abs((c[0]-d[0]) / (c[1]-d[1])) :
        return 1
    elif abs((a[0]-c[0]) / (a[1]-c[1])) == abs((b[0]-d[0]) / (b[1]-d[1])) :
        return 1
    elif abs((a[0]-d[0]) / (a[1]-d[1])) == abs((c[0]-b[0]) / (c[1]-b[1])) :
        return 1
    else :
        return 0
