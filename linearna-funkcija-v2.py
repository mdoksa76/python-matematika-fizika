import turtle
from datetime import datetime
from PIL import Image

# radni prozor, kornjaca i radna podloga
prozor=turtle.Screen()
prozor.setup(840,640)
prozor.title("Graf linearne funkcije y=ax+b.")
t=turtle.Turtle()
t.speed(0)
t.shape("circle")
t.shapesize(0.01)
podloga=turtle.getcanvas()

# skupljači koeficjenata linearnih funkcija u liste: aovi=a1,a2,a3,..., bovi=b1,b2,b3,...
global aovi
aovi=[]
global bovi
bovi=[]
global xovi
xovi=[]

# iscrtavanje radnog prozora
def kks():
    # okvir
    t.color("black")
    t.up()
    t.goto(-400,-300)
    t.down()
    t.goto(400,-300)
    t.goto(400,300)
    t.goto(-400,300)
    t.goto(-400,-300)

    # x-os (apscisa)
    t.up()
    t.goto(-400,0)
    t.down()
    t.goto(400,0)
    for i in range(-4,5):
        t.up()
        t.goto(i*100, -5)
        t.down()
        t.goto(i*100, 5)
        if i*100!=0 and i*100!=400:
            t.write(i*100)

    # y-os ordinata
    t.up()
    t.goto(0,-300)
    t.down()
    t.goto(0,300)
    for i in range(-3,4):
        t.up()
        t.goto(-5, i*100)
        t.down()
        t.goto(5, i*100)
        if i*100!=300:
            t.write(i*100)

    # strelice, X i Y
    t.up()
    t.goto(390,5)
    t.down()
    t.goto(400,0)
    t.goto(390,-5)
    t.up()
    t.goto(390,-20)
    t.write("X")
    t.up()
    t.goto(-5,290)
    t.down()
    t.goto(0,300)
    t.goto(5,290)
    t.up()
    t.goto(10,285)
    t.write("Y")
    t.ht()

#funkcija za crtanje grafa unutar okvira radnog prozora
def pravac(a,b):
    if a*(-400)+b<-300 or a*400+b>300:
        x1=int((-300-b)/a)
        if x1<-400:
            x1=-400
        x2=int((300-b)/a)
        if x2>400:
            x2=400
        print("\nCrtam funkciju y =", a, "× x +", b)
        print("od (", x1, ",", a*x1+b, ")", "do (", x2, ",", a*x2+b, ").\n")
        t.up()
        t.goto(x1, a*x1+b)
        if a<0:
            t.color("red")
        elif a>0:
            t.color("blue")
        elif a==0:
            t.color("green")
        else:
            print("Nedefinirani unos!")
        t.down()
        t.goto(x2, a*x2+b)
        t.write("p"+str(len(aovi)))
        t.ht()

    elif a*(-400)+b>300 or a*400+b<-300:
        x1=int((300-b)/a)
        if x1<-400:
           x1=-400
        x2=int((-300-b)/a)
        if x2>400:
           x2=400
        print("\nCrtam funkciju y =", a, "× x +", b)
        print("od (", x1, ",", a*x1+b, ")", "do (", x2, ",", a*x2+b, ").\n")
        t.up()
        t.goto(x1, a*x1+b)
        if a<0:
            t.color("red")
        elif a>0:
            t.color("blue")
        elif a==0:
            t.color("green")
        else:
            print("Nedefinirani unos!")
        t.down()
        t.goto(x2, a*x2+b)
        t.write("p"+str(len(aovi)))
        t.ht()

    else:
        print("\nCrtam funkciju y =", a, "× x +", b)
        print("od (", -400, ",", a*(-400)+b, ")", "do (", 400, ",", a*400+b, ").\n")
        t.up()
        t.goto(-400, a*(-400)+b)
        if a<0:
            t.color("red")
        elif a>0:
            t.color("blue")
        elif a==0:
            t.color("green")
        else:
            print("Nedefinirani unos!")
        t.down()
        t.goto(400, a*400+b)
        t.write("p"+str(len(aovi)))
        t.ht()

    if a<0:
        print("Funkcija y =", a, "× x +", b, "je padajuća.")
        print("Odsječak na osi y je u točci (0,", b, ").")
        print("Sjecište s osi x je u točci (", -b/a, ", 0).")
    elif a>0:
        print("Funkcija y =", a, "× x +", b, "je rastuća.")
        print("Odsječak na osi y je u točci (0,", b, ").")
        print("Sjecište s osi x je u točci (", -b/a, ", 0).")
    else:
        print("Funkcija y =", b, "je konstanta.")
        print("Odsječak na osi y je u točci (0,", b, ").")

def vpravac(x):
    t.color("grey")
    t.up()
    print("\nCrtam funkciju x =", x)
    print("od (", x, ",", "300)" , "do (", x, ",", "-300).\n")
    t.goto(x,300)
    t.down()
    t.goto(x,-300)
    t.up()
    t.goto(x,300)
    t.write("vp"+str(len(xovi)))
    t.ht()

# funkcija za izračun sjecišta 2 pravca
def s2p():
    print("\nNiz koeficijenata smjerova:", (aovi), "\nNiz odsječaka na ordinati:", (bovi))
    print("Uneseno je podataka o", len(aovi), "funkcija.\n")
    if len(aovi)<2 and len(bovi)<2:
        print("\nNema dvije linearne funkcije za trazenje njihovog sjecista.")
        print("Naredbom Insert unesi koeficijente bar dviju linearnih funkcija.\n")
    else:
        n1=int(input("Unesi redni broj prve funkcije: "))
        n2=int(input("Unesi redni broj druge funkcije: "))
        if n1>len(aovi) or n2>len(aovi):
            print("\nPogrešan unos. Provjeri broj unesenih funkcija.")
            print("Uneseno je", len(aovi), "funkcija.")
        else:
            if aovi[n1-1]==aovi[n2-1]:
                print("\nFunckije imaju isti koeficijent smjera, grafovi su im paralelni.")
                print("Ne sijeku se, odnosno, sijeku se u beskonačnosti.\n")
            else:
                xs=(bovi[n2-1]-bovi[n1-1])/(aovi[n1-1]-aovi[n2-1])
                ys=aovi[n1-1]*(bovi[n2-1]-bovi[n1-1])/(aovi[n1-1]-aovi[n2-1])+bovi[n1-1]
                print("Sjecište:", (xs,ys))
                t.up()
                t.color("black")
                t.goto(xs-1,ys-1)
                t.down()
                t.goto(xs+1,ys-1)
                t.goto(xs+1,ys+1)
                t.goto(xs-1,ys+1)
                t.goto(xs-1,ys-1)
                t.shapesize(0.01)
                t.up()
                t.goto(xs,ys)
                t.write("S"+str(n1)+str(n2))

# funkcija za izračun sjecišta pravca i vertikalnog pravca
def s2px():
    print("\nNiz koeficijenata smjerova:", (aovi), "\nNiz odsječaka na ordinati:", (bovi))
    print("\nNiz vertikalnih funkcija:", (xovi))
    if len(aovi)<1 and len(xovi)<1:
        print("\nPogrešan unos. Provjeri broj unesenih funkcija.")
        print("Uneseno je", len(aovi), "funkcija i", len(xovi), "vertikalnih funkcija.")
    else:
        n1=int(input("Unesi redni broj prve funkcije: "))
        n2=int(input("Unesi redni broj druge (vertikalne) funkcije: "))
        if n1>len(aovi) or n2>len(xovi):
            print("\nPogrešan unos. Provjeri broj unesenih funkcija.")
            print("Uneseno je", len(aovi), "funkcija.")
            print("Uneseno je", len(xovi), "vertikalnih funkcija.")
        else:
            xs=(xovi[n2-1])
            ys=aovi[n1-1]*xs+bovi[n1-1]
            print("Sjecište:", (xs,ys))
            t.up()
            t.color("black")
            t.goto(xs-1,ys-1)
            t.down()
            t.goto(xs+1,ys-1)
            t.goto(xs+1,ys+1)
            t.goto(xs-1,ys+1)
            t.goto(xs-1,ys-1)
            t.shapesize(0.01)
            t.up()
            t.goto(xs,ys)
            t.write("Sv"+str(n1)+str(n2))

# funkcija za spremanje datoteke 
def spremisliku():
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
    datoteka = "graf-" + date
    graf=turtle.Screen()
    graf.getcanvas().postscript(file=datoteka+".eps")
    img = Image.open(datoteka + ".eps") 
    img.save(datoteka + ".jpg")
    print("\nSnimljene su datoteke:", datoteka + ".jpg i", datoteka + ".eps" + ".")

# unos nove jednadžbe pravca
def novi_graf():
    a=float(input("\na = "))
    aovi.append(a)
    b=float(input("b = "))
    bovi.append(b)
    print("\nLinearna funkcija: y =", a, "x + ", b)
    print("\nNiz a-ova i b-ova:", (aovi, bovi))
    print("\nNiz x-ova:", xovi)
    pravac(a,b)

def novi_xgraf():
    x=float(input("\nx = "))
    xovi.append(x)
    print("\nNiz x-ova:", xovi)
    print("\nNiz a-ova i b-ova:", (aovi, bovi))
    vpravac(x)

# čisti, novi prozor
def novi_prozor():
    t.clear()
    print("\nObrisao sam ekran ...")
    kks()
    print("... evo, novi ekran spreman je za crtanje grafova.\n")
    aovi.clear()
    bovi.clear()
    xovi.clear()
    pomoc()

# izlaz iz programa
def izlaz():
    f=open("funkcija-ab.txt", "r")
    sadrzaj=f.read()
    print(sadrzaj)
    f.close()
    print("\nCiao bella!")
    prozor.bye()

def pomoc():
    print("_______________________________________________________________________\n")
    print("Pomoć za Python program - Graf linearne funkcije y=ax+b.")
    print("_______________________________________________________________________\n")
    print("Kontrolne tipke: Insert, X, S, Y, End, Delete i Esc.\n")
    print("Insert - unos koeficijenata a i b linearne funkcije\n")
    print("X - unos vrijednosti x vertikalnog pravca\n")
    print("S - Izračun koordinata točke sjecišta dvije linearne funkcije (pravaca)\n")
    print("Y - Izračun koordinata točke sjecišta dvije linearne funkcije (pravaca)\nod kojih je jedna vertikalna\n")
    print("End - snimanje slike nacrtanog grafa (grafova)\n")
    print("Delete - brisanje nacrtanog prozora\n")
    print("Esc - izlaz iz programa\n")
    print("_______________________________________________________________________\n")

# osluškivanje komandi
prozor.listen()

# u iščekivanju Godota, pardon snimanja datoteke
prozor.onkey(spremisliku, "End")

# unos nove linearne funkcije
prozor.onkey(novi_graf, "Insert")

# unos vertikalnog pravca
prozor.onkey(novi_xgraf, "x")

# brisanje nacrtanih grafova
prozor.onkey(novi_prozor, "Delete")

# izračun točke sjecišta 2 pravca
prozor.onkey(s2p, "s")

# izračun točke sjecišta pravca i vertikalnog pravca
prozor.onkey(s2px, "y")

#izlaz iz programa
prozor.onkey(izlaz, "Escape")

# ispis pomoći i crtanje radnog prozora, kks = Kartezijev koordinatni sustav
pomoc()
kks()

#testni uzorak pravaca
#pravac(0.75,-25)
#pravac(0.75,25)
#pravac(-0.75,25)
#pravac(-0.75,-25)
