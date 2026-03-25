def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"


def onderstreep(tekst = ""):
      uit = []
      uit.append(tekst)
      uit.append(len(tekst)*"=")
      return uit 


inkomsten = {
    "Aardbeien-ijs-totaal" : 1000, 
    "Vanille-ijs-totaal" : 2000, 
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

def som(dict):
    totaal = 0 
    for i in dict:
        totaal += i
    return totaal
