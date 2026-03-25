'''
mijn_dict = {
    'vis' : 10,
    'vlees' : 25, 
    'overig' : 15
}

totaal = 50
'''

def presenteer(mijn_dict, totaal):
    for k,v in mijn_dict.items():
        print (f"{k} : {v} euro")
    print ("="*25)  
    print(f"totaal : {totaal} euro")


#presenteer(mijn_dict,totaal)