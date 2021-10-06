import time
import random
print('''-------------------------------------
welkom het bij het adventure spel
----------------------------------------
''')
def stop():
    ("je hebt het spel verloren")
    quit()
spelen_JA = input("wil je spelen? ").lower() =='nee'
if spelen_JA:
    print("jammer fijnen dag")
    quit()
# hier begin ik met de eerste stuk
def begin():
    kant = input('''
    je loopt naar buiten en je begint je avontuur om melk te halen?
    Ga je rennen? J/N
    ''').lower() =='j'
    if kant:
        print('je wordt moe en gaat dood')
        stop()
    if kant == False:
        print(''''-----------
        goed gedaan
        --------------''')

def begin2():
    print('''----------------------------------
    je hebt het eerste spel gehaald mooiso
    ------------------------------
    ''')
    monster = input('''je ziet een monster wat doe je?
    a  rennen
    b vechten 
    c negeren
    ''').lower() =='c'
    if monster == False:
        print('je bent niet in een goede staat en je faalt ')
        stop()
def middenstuk():
    man = input(''''-----------------
    je loopt door en je ziet een man die een mol eet wat doe je?
    a je eet met hem mee
    b je rent weg 
    c je loopt door
    -----------------------------------
    ''').lower() in ['b' 'c']
    if man:
        achterna  =  input("de man komt achter je na val je aan? J/N") =='J'
        if achterna:
            print('de man vermoord je omdat je hem aanviel')
            stop()
        else:
            print('''--------------------
            de man vraagt of je een hapje wil en je hebt honger dus je zegt ja
            -----''')

def einde1():
    fast_travel = input('''--------------------------
    je hebt lekker met hem gegeten en nu vraagt hij of je snel naar de supermarkt wil ga je mee J/N
    ps je bent erg moe
    ''').lower() == 'j'
    if fast_travel:
        print('''
        ---------------------------------------------------------------
        je bent aangekomen gefeliciteert de man bedankt voor het spelen
        ------------------------------------------
        
        ''')
    
    else:
        stop()
def einde2():
    time.sleep(5)
    print('''
    ------------------------------------
    ha dat dacht je de man heeft je namelijk opgelicht en je naar de verkeerde supermarkt gestuurd.
    Ook heeft je vrouw meegenomen en bedreigd je met dat als je geen mol hem vangt dat hij haar dood.
    je krijgt 10 keer de kans om een mol te vangen
    dit kan door een getal te kiezen
 
    
    ''')
    getal = random.randint(1,10)
    for j in range(10,1,-1):
        het_getal = int(input('kies een getal? '))
        if het_getal == getal:
            print(''''
            -----------------------
            goedzo je hebt het spel afgespeeld 
            deze keer echt 
            ---------------------------
        

            ''')
            break
        else:
            print('probeer het opnieuw')
begin()
begin2()
middenstuk()
einde1()
einde2()
