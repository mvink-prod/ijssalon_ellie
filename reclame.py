from algemene_functies import mijn_functie_2

# vraag 5 
def aanbieding_1(smaak,prijs,korting):
    nieuwe_prijs = prijs - prijs * korting
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro.")
    
#print(aanbieding_1("aardbei",4,0.1))    

# vraag 6 & 7
def inkomsten_totaal(inkomsten, btw):
    totaal = 0 
    max_range = len(inkomsten)
    for i in range (0,max_range):
        totaal += inkomsten[i]
        bedrag = totaal*btw
    return(f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden.")
    
#print(inkomsten_totaal([220,430,125,160,205,90,345],0.09))

#vraag 8 
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return(hoogste, laagste)


#print(laag_en_hoog([350,122,95,880,250]))

# vraag 9 & 10
def gemiddelde(mijn_lijst):
    totaal = 0 
    max_range = len(mijn_lijst)
    for i in range (0,max_range):
        totaal += mijn_lijst[i] 
    bedrag = (totaal/max_range)     
    return(f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro.")   

#print(gemiddelde([220,430,125,160,205,90,345]))

# vraag 11

def meervoudig(invoer_lijst):
    lengte_invoer_lijst = len(invoer_lijst)
    if lengte_invoer_lijst <= 4:
        return("Invoerlijst is te kort")
    if lengte_invoer_lijst in range (5,11):
        return(laag_en_hoog(invoer_lijst))
    if lengte_invoer_lijst > 10:
        return("Invoerlijst is te lang")

#print(meervoudig([15,5,6,780,880,6,55,85,45,66]))

# vraag 12 
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return(mijn_functie_2(korte_lijst[0],korte_lijst[1]))

print(combinatie([10,5,3,2,1,2,9]))