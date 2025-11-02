def solution(balls, share):
    n_, n_m, m_ = 1, 1, 1
     
    for i in range(1, balls+1):
        n_ *=i
    for i in range(1, balls-share+1):
        n_m *=i
    for i in range(1, share+1):
        m_*=i
    
    return n_/(n_m*m_)