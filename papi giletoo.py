print(''''
----------------------------------------------
Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.
---------------------------------------------------------

''')
def Bakje(aantal):
    bakje = input('wilt u deze '+ str(aantal) + ' bolletje(s) in A) een hoorntje of B) een bakje? ').lower()
    return bakje
def Aantal_bolletjes():
    bolletjes = int(input('hoeveel bolletjes wil je? '))
    return bolletjes
def checkout(bakje,aantal2):
    answer = input('Hier is uw '+bakje +' met '+ str(aantal2)+' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    return answer
def werking():
    while True:
        bolletjes = Aantal_bolletjes()
        
        if bolletjes >= 1 and bolletjes <= 3:
            bakofhoorn = Bakje(bolletjes)
            if bakofhoorn =='a':
                b = checkout('hoorn',bolletjes)
                if b == 'n':
                    print('tot ziens')
                    quit()
                
            if bakofhoorn =='b':
                a = checkout('bakje',bolletjes)
                if a == 'n':
                    print('tot ziens')
                    quit()
                
        if bolletjes >=4  and bolletjes <= 8:
            c = checkout('bakje',bolletjes)
            if c == 'n':
                print('tot ziens')
                quit()
            
            if bolletjes > 8:
                print('we niet zo een formaat bakje ')
        
        
        else:    
            print('dit begrijp ik niet')
        
            
    
    
werking()



    
    
    
        
           
