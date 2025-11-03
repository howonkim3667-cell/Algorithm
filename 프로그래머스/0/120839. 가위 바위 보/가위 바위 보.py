def solution(rsp):
    answer = ''
    a=list(rsp)
    win = {'2': '0', '0':'5', '5':'2'}
    for i in a:
        answer += win[i]
    
    return answer

# 가위 : 2
# 바위 : 0
# 보   : 5