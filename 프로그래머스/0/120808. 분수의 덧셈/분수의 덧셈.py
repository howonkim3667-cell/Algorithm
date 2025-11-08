def solution(numer1, denom1, numer2, denom2):
    # 분수의 합 answer[0]분자 answer[1] 분모
    answer = [numer1*denom2 + numer2*denom1 ,  denom1*denom2]
    
    # 분모와 분자의 최대공약수
    a , b = answer[0], answer[1]
    while b !=0:
        temp = a
        a = b
        b = temp % b
        
    answer[0] = answer[0]//a
    answer[1] = answer[1]//a
    
    return answer
        
    
