from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    aftreksel=prijs*korting
    a=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-aftreksel} euro."
    return a

def inkomsten_totaal(inkomsten, btw):
    totaal=0
    for nr in inkomsten:
        totaal=totaal+nr
    totaal_btw=totaal*btw
    a=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal_btw} euro btw betaald dient te worden."
    return a

def laag_en_hoog(mijn_lijst):
    w=str(max(mijn_lijst))+ " " + str(min(mijn_lijst))
    w2=list(w.split(" "))
    w3=list(map(int, w2))
    return w3

def gemiddelde(mijn_lijst):
    tot=0
    for nr in mijn_lijst:
        tot=tot+nr
    gem=tot/len(mijn_lijst)
    gemtxt=f"De gemiddelde inkomsten deze week zijn {gem} euro."
    return gemtxt

def meevoudig(invoer_lijst):
    a=laag_en_hoog(invoer_lijst)
    return a

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
