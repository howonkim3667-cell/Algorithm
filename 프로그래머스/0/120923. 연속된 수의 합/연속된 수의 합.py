def solution(num, total):
    cur = []
    a = 0
    b = -1
    if num == 1:
        while True:
            cur.append(a)
            if sum(cur) == total:
                return cur
            a+=1 
            cur.clear()
    else:
    
        while True:
            for i in range(num):
                cur.append(a)
                a += 1     
            if sum(cur)>total:

                while True:
                    cur.pop()
                    cur.append(b)
                    cur.sort()
                    if sum(cur) == total:
                        cur.sort()
                        return cur
                    b -= 1
            if sum(cur) == total:
                break
            else:
                a=cur[1]
            cur.clear()
        cur.sort()
        return cur