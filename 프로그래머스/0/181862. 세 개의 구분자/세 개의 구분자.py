def solution(myStr):
    answer = ["a", "b", "c"]
    for i in answer:
        myStr = myStr.replace(i," ")
    a = myStr.strip().split()
    if len(a) == 0:
        return ['EMPTY']
    return  a