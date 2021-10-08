print(''''
----------------------------------------------
Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.
---------------------------------------------------------

''')
def Bakje(aantal):
    bakje = input('wilt u deze '+ str(aantal) + ' bolletje(s) in A) een hoorntje of B) een bakje?')
    return bakje
def Aantal_bolletjes():
    bolletjes = int(input('hoeveel bolletjes wil je? '))
    return bolletjes
def checkout(bakje,aantal2):
    input('Hier is uw '+bakje +' met '+ str(aantal2)+' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
def werking():
    while True:
        while True:
            bolletjes = Aantal_bolletjes()
            ijs_plaatsing = Bakje(bolletjes)
            if bolletjes >= 1 and bolletjes <= 3:
                ijs_plaatsing = Bakje(bolletjes)
                break 
            if bolletjes >= 4 and bolletjes <= 8:
                bon = checkout('bakje',bolletjes)
                break
            if bolletjes > 8:
                print('zoveel passen niet in 1 bak')
            else:
                print('ik begrijp het niet')
        while True:
            if ijs_plaatsing == 'a':
                bon2 = checkout('hoorn',bolletjes)
                break
            if ijs_plaatsing == 'b':
                bon3 = checkout('bakje',bolletjes)
                break
            else:
                print('ik begrijp dit niet')
        while checkout == False:
            if checkout =='j':
                print('herstarten')
            if checkout =='nee':
                print('tot ziens en eetsmakelijk')
                break
            else: 
                print('ik begrijp dit niet ')
    
werking()         
    