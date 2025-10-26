def solution(chicken):
    coupon =[]
    b= chicken
    while True:
        quo, rem= divmod(b,10)
        coupon.append(quo)
        b=quo +rem
        if not quo :
            break
    return sum(coupon)    