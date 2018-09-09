# -*- coding: utf-8 -*-
import time
print("Velkommen til Pengemesteren! I dette spillet vil kun de beste gamblerene vinne!")
time.sleep(5)
print("Reglene er som følger:\nDu begynner med 200kr. Målet med spillet er å nå 1000kr før spillets slutt. Går du tom for penger har du tapt.")
print("Pengemesteren består av 10 runder, og du har i hver runde mulighet til å tjene mer penger.")
time.sleep(3)
print("Er du klar?\nRunde 1 er i ferd med å begynne!:")
 
a=int(200)
    


b=input("Du møter en mann som utfordrer deg til et veddemål.\nHvis du vinner tjener du 300kr, hvis du taper mister du 100.\nTar du utfordringen?")

if b=="NEI":
    print("Du har avslått tilbudet.")
    
elif b=="JA": 
    print("Du har takket ja til veddemålet!")
    time.sleep(3)
    import random
    for x in range(1,2):
        x=random.randint(1,2)
    if x==1: 
        print("Du tapte veddemålet, ny saldo er",a,"kr")
        a-=100
    else:
        a+=300
        print("Gratulerer du vant veddemålet! Ny saldo er" , a, "kr!")
time.sleep(3)

if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
        
        
andre=input("Du vurderer å kjøpe et flaxlodd for 25kr. Vil du kjøpe loddet?")

if andre=="NEI":
    print("Du har avslått tilbudet.")
    time.sleep(3)
    
elif andre=="JA": 
    print("Du har takket ja til veddemålet!")
    time.sleep(3)
    
    for x in range(1,3):
        x=random.randint(1,3)
    if x==1: 
        a-=25
        print("Ingen gevinst, ny saldo er",a,"kr")
        
    elif x==2: 
        a+=25
        print("Gratulerer du vant 50kr! Ny saldo er" , a, "kr!")
        
    else: 
        a+=75
        print("Gratulerer, du tok førstepremien og vant 100kr! Ny saldo er", a, "kr")
time.sleep(3)

if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
        

tredje=input("En venn spør om å låne 80kr. Han sier at han vil gi tilbake det dobbelte. Stoler på vedkommende?")

if tredje=="NEI":
    print("Du har avslått tilbudet.")
    
elif tredje=="JA": 
    print("Du har takket ja til veddemålet!")
    time.sleep(3)
    for x in range(1,2):
        x=random.randint(1,2)
    if x==1:
        a-=80
        print("Vennen din stakk av med pengene. Ny saldo er",a, "kr.")
    
    else:
        a+=160
        print("Nå var du heldig! Vennen din overførte 160kr. Ny saldo er" , a, "kr!")
time.sleep(3)
if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
        
        
fjerde=input("Du får tilbudet om å hente en klassekamerat med bil. Du får 100kr hvis du tar jobben, men du har ikke lappen. Tar du sjansen? ")

if fjerde=="NEI":
    print("Du har avslått tilbudet.")
    
elif fjerde=="JA": 
    print("Du henter vennen din!")
    time.sleep(3)
    
    for x in range(1,2):
        x=random.randint(1,2)
    if x==1:
        a-=250
        print("Du ble stoppet av politiet, og må betale en bot på 250kr. Ny saldo er",a,"kr.")
        
    else:
        a+=100
        print("Du slapp unna politiet. Vennen din overførte 100kr. Ny saldo er",a, "kr")
        time.sleep(3)
        
if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
        
femte=input("Du er ute på tur og kommer til et kryss. Her kan du velge mellom en grusvei og en sti. Vil du gå grusveien")

if femte=="JA":
    a-=50
    print("Du valgte grusveien. Her ble du robbet for 50kr. Resten av pengene dine gjemte du i et skjult rom i sekken. Ny saldo er", a, "kr")
    
elif femte=="NEI": 
    a+=45
    print("Gratulerer! Du valgte den mindre traffikerte stien. Her fant du en lommebok med en finnerlønn på 45kr! Ny saldo er",a,"kr.")
    time.sleep(3)
    
if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
    
    
sjette=input("Liverpool skal spille hjemmekamp mot Chelsea. Du kan tippe på uavgjort,U, hjemmeseier,H, eller borteseier,B. Du setter 100kr. Hvem gjetter du på?")

if sjette=="H": 
    print("Du spår at Liverpool vinner.")
    time.sleep(4)
    
    for x in range(1,3):
        x=random.randint(1,3)
    if x==1:
        a+=200
        print("Gratulerer. Liverpool vant kampen. Ny saldo er", a, "kr.")
    else: 
        a-=100
        print("Liverpool vant desverre ikke kampen. Ny saldo er", a, "kr.")
        
elif sjette=="U":
    print("Du spår at lagene spiller uavgjort.") 
    time.sleep(4)
    for x in range(1,3):
        x=random.randint(1,3)
    if x==2:
        a+=200
        print("Gratulerer. Lagene spilte uavgjort. Ny saldo er", a, "kr.")
    else: 
        a-=100
        print("Liverpool vant kampen. Ny saldo er", a, "kr.")
        
elif sjette=="B":
    print("Du spår at Chelsea vinner kampen.") 
    time.sleep(4)
    for x in range(1,3):
        x=random.randint(1,3)
    if x==3:
        a+=200
        print("Gratulerer. Chelsea vant i en jevn kamp. Ny saldo er", a, "kr.")
    else: 
        a-=100
        print("Liverpool vant kampen. Ny saldo er", a, "kr.")
        
if a>=1000: 
    print("Gratulerer, du er en ekte pengemester!")

elif a<=0: 
    print("Bedre lykke neste gang!")
        
        

    
    
    
        


        
    
        
        

        

        
   

