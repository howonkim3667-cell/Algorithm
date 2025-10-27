def solution(arr):
    
    current = list(arr)
    count= 0
    while True :
        prev = list(current)

        temp = list(current)
        for i in range(len(arr)):
            if temp[i]>=50 and not temp[i]%2:
                temp[i] = int(temp[i]/2)
            elif temp[i]<50 and temp[i]%2:
                temp[i] = (temp[i]*2)+1
        
        current = list(temp)
        if  prev == current:
            return count                
        count+=1
