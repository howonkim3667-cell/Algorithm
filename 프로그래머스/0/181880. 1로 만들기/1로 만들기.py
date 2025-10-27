def solution(num_list):
    
    count_list =[]
    for i in num_list:
        count = 0
        a = i
        while a != 1:
            if a%2:
                a = int((a-1)/2)
            else:
                a  = int(a/2)
            count+=1
        count_list.append(count)
    return sum(count_list)