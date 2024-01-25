def mijn_functie_1(a):
    a=a*a
    return a

def mijn_functie_2(a,b):
    w1=a+b
    w2=a-b
    w3=a*b
    w4=a/b
    w5=f"{w1} {w2} {w3} {w4}"
    w6=list(w5.split(" "))
    w7=list(map(float, w6))
    return w7
