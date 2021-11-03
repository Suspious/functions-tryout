
# this is a print screen that it wil give in the beginning
from typing import AsyncGenerator


print(''''
----------------------------------------------
Welkom bij Papi Gelato 
---------------------------------------------------------

''')
#items = ['bolletjes','bakjes','hoorntje','chocolade sause'vanille saus','aardbeien saus','munt']
#Stap 1
vanille = 0
Chocolade = 0 
munt = 0 
bak = 0
hoorn = 0
def bakofhoorn():
    Bak_hoorn = input('wil je een bakje of hoorntje? ')
    return Bak_hoorn

def bolletje():
    bol = int(input('hoeveel bolletjes wil je? '))
    return bol
def saus():
    smaken = input('''
    ---------------------------
    welke saus wil je daarop?
    ---------------------------
    a Chocolade
    b vanille 
    c munt
    d geen 
    ''')
    if smaken=='a':
        smaken= 'chocolade'
    if smaken =='b':
        smaken = 'vanille'
    if  smaken =='c':
        smaken = 'munt'
    return smaken
Aantal_bolletjes = bolletje()
if Aantal_bolletjes >= 1 and Aantal_bolletjes <= 4:
    welkesaus = saus()
    if welkesaus =='chocolade':
        Chocolade + 1
    if welkesaus =='vanille':
        vanille + 1
    if welkesaus =='munt':
        munt + 1
    bakkie = bakofhoorn()
    if bakkie =='bak':
        bak = bak + 1
    if bakkie =='hoorn':
        hoorn = hoorn + 1
    
if Aantal_bolletjes >= 5 and Aantal_bolletjes <= 8:
    welkesaus = saus()
    bak = bak + 1
    if welkesaus =='chocolade':
        Chocolade + 1
    if welkesaus =='vanille':
        vanille + 1
    if welkesaus =='munt':
        munt + 1 
else:
    print('ik begrijp dit niet')
if Aantal_bolletjes > 8:
    print('je kan niet zo een groot ijsje kiezen')
saus =[{'naam':'Chocolade','aantal':Chocolade},{'naam':'munt','aantal':munt},{'naam':'vanille','aantal':vanille}]

def bon(bolletje,saus,bak,hoorn):
    prijsbolletje = bolletje * 1.1
    print(bolletje,' x 1.10    = ',prijsbolletje )
    prijshoorntje = hoorn * 1.25
    print('hoorn   ',hoorn,' x 1,25  =   ',prijshoorntje)
    prijsbak = float(bak) * 0.75
    print('bak   ',bak,' x 0,75  =  ',prijsbak )
    for sausie in range(4):
        prijssaus = saus[sausie]['aantal'] * 0.75
        aantal = saus[sausie]['aantal']
        naamsaus = saus[sausie]['naam']
        print(naamsaus, aantal,'x   = ',prijssaus)
bon(Aantal_bolletjes,saus,bak,hoorn) 

     
        







    





    
