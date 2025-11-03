# def solution(babbling):
#     a =["aya", "ye", "woo", "ma"]
#     c =0
#     for i in a:
#         for j in babbling:
#             if i in j:
#                 c+=1
#     return c

def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c


# def solution(babbling):
#     a =["aya", "ye", "woo", "ma"]
#     combi =[]
#     count = 0
#     for i in range(len(a)):
#         for j in range(len(a)):
#             combi.append(a[i]+a[j])
#             for z in range(len(a)):
#                 combi.append(a[i]+a[j]+a[z])
#                 for b in range(len(a)):
#                     combi.append(a[i]+a[j]+a[z]+a[b])
#     combi +=a
#     for i in babbling:
#         if i in combi:
#             count +=1
#     return count