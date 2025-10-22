def solution(order):
    a=0

    menu =[
        ["iceamericano", 
            "americanoice", 
            "americano", 
            "hotamericano", 
            "americanohot", 
            "anything"],

        ["icecafelatte", 
            "cafelatteice", 
            "hotcafelatte", 
            "cafelattehot",
            "cafelatte", 
            "hotcafelatte", 
            "cafelattehot"]
        ]
    
    for i in order:
        if i in menu[0]:
            a+=4500
        else:
            a+=5000
    return a
            
        
     