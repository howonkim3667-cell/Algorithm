def solution(arr, delete_list):
    for i in delete_list:
        try:
            a=arr.index(i)
        except:
            continue
        arr.pop(a)
        
    return arr