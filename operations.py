from math import gcd

def somme_rationnels(a,b):
    [N_a,D_a],[N_b,D_b] = a,b
    s = [N_a*D_b+N_b*D_a,D_a*D_b]
    c = gcd(s[0],s[1])
    return [int(s[0]/c),int(s[1]/c)]

def produit_rationnels(a,b):
    [N_a,D_a],[N_b,D_b] = a,b
    s = [N_a*N_b,D_a*D_b]
    c = gcd(s[0],s[1])
    return [int(s[0]/c),int(s[1]/c)]
    
def produit_polynomes(P,Q):
    n,p = len(P),len(Q)
    s = []
    for i in range(n+p-1):
        coeff = [0,1]
        for k in range(i+1):
            if k < len(P) and i-k < len(Q):
                coeff = somme_rationnels(coeff,produit_rationnels(P[k],Q[i-k]))
        s += [coeff]
    return s

def somme_polynome(P,Q):
    s = []
    for i in zip(P,Q):
        s += [somme_rationnels(i[0],i[1])]
    p,q = len(P),len(Q)
    if p>q:
        P,Q,p,q = Q,P,q,p
    if p<q:
        s += Q[p:]
    return s

def produit_scalaire_polynome(scalaire,poly):
    for i in range(len(poly)):
        stock = produit_rationnels(poly[i],scalaire)
        s = gcd(stock[0],stock[1])
        poly[i] = [int(stock[0]/s),int(stock[1]/s)]
    return poly










