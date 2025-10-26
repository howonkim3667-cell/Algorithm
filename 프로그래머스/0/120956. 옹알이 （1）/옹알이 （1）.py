def solution(babbling):
    a =["aya", "ye", "woo", "ma"]
    combi =[]
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            combi.append(a[i]+a[j])
            for z in range(len(a)):
                combi.append(a[i]+a[j]+a[z])
                for b in range(len(a)):
                    combi.append(a[i]+a[j]+a[z]+a[b])
    
    
    combi +=a
    print(combi)
    for i in babbling:
        if i in combi:
            count +=1
    
    return count