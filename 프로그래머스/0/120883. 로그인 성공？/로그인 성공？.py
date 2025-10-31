def solution(id_pw, db):
    a, b = id_pw
    for info in db:
        i, p = info
        if a ==i and b ==p:
            return "login"
    for info in db:
        i, p = info
        if a ==i and b !=p:
            return "wrong pw"
    # for info in db:
    #     i, p = info
    #     if a ==i or b ==p:
    #         return "wrong pw"
    return "fail"