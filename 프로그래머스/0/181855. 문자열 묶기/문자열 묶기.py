def solution(strArr):
    a = {}
    for i, v in enumerate(strArr):
        strArr[i] = len(v)

    for i in strArr:
        a[i] = a.get(i, 0)+1
    
    a_m = max(a, key=a.get) # 키를 기준으로 값을 가져와서 맥스값 추출
    return a[a_m]