

print(''''
----------------------------------------------
Welkom bij Papi Gelato 
---------------------------------------------------------

''')
bol = 0
toppingaantal = 0 
toppingprijs =  0
vanille = 0
Chocolade = 0 
munt = 0 
bak = 0
hoorn = 0
liter = 0
vanille2 = 0
Chocolade2 = 0
munt2 = 0  

def bolletje():
    global bol
    bolje = int(input('hoeveel bolletjes wil je? '))
    bol = bol + bolje
    return bol
def bakofhoorn():
    global bak 
    global hoorn
    Bak_hoorn = input('wil je een bakje of hoorntje? ').lower()
    if Bak_hoorn =='bakje':
        bak = bak + 1
    if bakofhoorn == 'hoorntje':
        hoorn = hoorn + 1 
    return Bak_hoorn
def topping():
    global toppingaantal
    global toppingprijs
    global bakofhoorn
    bak = bakofhoorn
    top = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ').lower()
    if top =='b':
        toppingaantal = toppingaantal + 1
        toppingprijs = toppingaantal * 0.50
    if top =='d' and bak =='bakje':
        toppingaantal = toppingaantal + 1
        toppingprijs = toppingaantal * 0.60
    if top =='d' and bak =='hoorntje':
        toppingaantal = toppingaantal + 1
        toppingprijs = toppingaantal + (top * 0.90)
    if top =='c':
        toppingaantal = toppingaantal + 1
        toppingprijs = toppingaantal * 0.30
    

def saus():
    global munt 
    global Chocolade
    global bolletje
    global vanille
    global Chocolade2
    global vanille2 
    global munt2 
    smaken = input('''
    
    ---------------------------
    welke saus wil je daarop?
    ---------------------------
    a Chocolade
    b vanille 
    c geen 
    ''').lower()
    if smaken =='a':
        Chocolade2 = Chocolade2 + 1
        Chocolade = bol + Chocolade
        

        
    if smaken =='b':
        vanille2 = vanille2 + 1
        vanille = vanille + bol
    else: 
        print('Sorry dat is geen optie die we aanbieden...')
def liter():
    global saus
    liter30 = 0
    liters = int(input('hoeveel liter wil je?  '))
    liter30 = liters + liter30
    while liter30 > 0:
        saus()
        liter30 = liter30 - 1
        if liter30 == 0:
            break
    return liters
    

def bon(hoorn,bak,bol):
    global Chocolade
    global munt
    global vanille
    global toppingaantal
    global toppingprijs
    saus =[{'naam':'Chocolade','aantal':Chocolade},{'naam':'munt','aantal':munt},{'naam':'vanille','aantal':vanille}]
    prijsbolletje = bol * 0.95 
    
    print('bol  ',bol,' x 1.10    = ', format(prijsbolletje, '.2f'))
    prijshoorntje = hoorn * 1.25
    print('hoorn   ',hoorn,' x 1,25  =   ',prijshoorntje)
    prijsbak = float(bak) * 0.75
    print('bak   ',bak,' x 0,75  =  ',prijsbak )
    for sausie in range(3):
        totaalsaus = Chocolade + munt + vanille
        totaal = totaalsaus * 0.75
        prijssaus = saus[sausie]['aantal'] * 0.75
        aantal = saus[sausie]['aantal']
        naamsaus = saus[sausie]['naam']
        print(naamsaus, aantal,'x 0,75  = ',prijssaus)
    
    print(toppingaantal,' toppings kosten ',format(toppingprijs, '.2f'))    
    totaal1 = prijshoorntje + prijsbak + totaal + prijsbolletje
    
    print('totaal   =  ',format(totaal1, '.2f'))

zakelijk_particulier = input('ben je zakelijk of particulier \n').lower()
while zakelijk_particulier =='particulier':
    bollie = bolletje()
    if bollie >= 1 and bollie <= 4:
        saus()
        topping()
        bakofhoorn()
        keren = input('wil je nog meer bestellen? ')
    if keren =='nee':

        bon(hoorn,bak,bol)
        break
                
    if bollie >= 5 and bollie <= 8:
        saus()

        print('je krijgt automatisch een bak')
        topping()
        bak = bak + 1
        keren = input('wil je nog meer bestellen? ')
        if keren =='nee':
            bon(hoorn,bak,bol)
            break
            
    if bollie > 8:
        print('zo groot past er niet in 1 bak of hoorn')
        keren = input('wil je nog meer bestellen? ')
        if keren =='nee':
            bon(hoorn,bak,bol)
            break
    else:
        print('Sorry dat is geen optie die we aanbieden...')

while zakelijk_particulier =='zakelijk':
    aantal = liter()
    aantalprijs = aantal * 9.80
    for sausie in range(3):
        saus2 =[{'naam':'Chocolade','aantal':Chocolade2},{'naam':'munt','aantal':munt2},{'naam':'vanille','aantal':vanille2}]
        totaalsaus = Chocolade2 + munt2 + vanille2
        totaal = totaalsaus * 0.75
        prijssaus = saus2[sausie]['aantal'] * 0.75
        aantal = saus2[sausie]['aantal']
        naamsaus = saus2[sausie]['naam']
        print(naamsaus, aantal,' x 0,75  = ',prijssaus)
        totaalprijs = totaal + aantalprijs
    print('liters  ',format(aantal, '.2f'),' x 9.8    = ',format(aantalprijs, '.2f'))

    print('totaal      = ',format(totaalprijs,'.2f'))
    btw = (totaalprijs / 100) * 6

    print('btw (%9)  = ',btw)
    break


