def solution(polynomial):
    answer = ''
    const= 0
    x= 0
    for i in polynomial.replace('+', "").split():
        print(i)
        if i.isdigit():
            const+=int(i)
        elif i.isalpha():
            x += 1
        else:
            print("ad",i.replace('x',""))
            x += int(i.replace('x',""))
        print(const, x)        
        
    print(const, x)
    
    if x==0:
        return str(const)
    elif x==1 and const==0:
        return str('x')
    elif x==1 and not const==0:
        return f'x + {const}'
    elif not x==0 and const==0:
        return f'{x}x'
    elif not x==0 and not const==0 :
        return f'{x}x + {const}'

        
    return answer