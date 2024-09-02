import turtle
from datetime import datetime
from PIL import Image

# radni prozor, kornjaca i radna podloga
prozor=turtle.Screen()
prozor.setup(802,602)
prozor.title("Graf kvadratne funkcije y=ax**2+bx+c.")
t=turtle.Turtle()
t.speed(0)
t.shape("circle")
t.shapesize(0.01)
t.up()
podloga=turtle.getcanvas()

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
            t.up()

    # y-os ordinata
    t.up()
    t.goto(0,-300)
    t.down()
    t.goto(0,300)
    t.up()
    for i in range(-3,4):
        t.up()
        t.goto(-5, i*100)
        t.down()
        t.goto(5, i*100)
        if i*100!=300:
            t.write(i*100)
            t.up()

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
    t.up()
    t.ht()

#funkcija za crtanje grafa unutar okvira radnog prozora
def graf(a,b,c):
    t.color("blue")
    t.goto(-400,a*(-400)**2+b*(-400)+c)
    for x in range(-400,400,5):
        t.down()
        t.goto(x,a*x**2+b*x+c)
        t.up()

    #for x in range(-400, 400+1):
        #tocke=[]
        #t.up()
        #y=a*x**2+b*x+c
        #t.down()
        #t.goto(x,y)
        #tocke.append([x,y])
        #print(tocke)
        #t.ht()

# funkcija za spremanje datoteke 
def spremisliku():
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
    datoteka = "graf-" + date
    graf=turtle.getscreen()
    graf.getcanvas().postscript(file=datoteka+".eps")
    img = Image.open(datoteka + ".eps") 
    img.save(datoteka + ".jpg")
    print("\nSnimljene su datoteke:", datoteka + ".jpg i", datoteka + ".eps" + ".")

# unos nove jednadzbe kvadratne funkcije
def novi_graf():
    a=float(input("\na = "))
    b=float(input("b = "))
    c=float(input("b = "))
    print("\nKvadratna funkcija: y =", a, "x**2 +", b, "x +", c)
    graf(a,b,c)

# cisti, novi prozor
def novi_prozor():
    t.clear()
    print("\nObrisao sam ekran ...")
    kks()
    print("... evo, novi ekran spreman je za crtanje grafova.\n")
    pomoc()

# izlaz iz programa
def izlaz():
    print("\nPozdrav!")
    prozor.bye()

def pomoc():
    print("_______________________________________________________________\n")
    print("Pomoc za Python program - Graf kvadratne funkcije y=ax**2+bx+c.")
    print("_______________________________________________________________\n")
    print("Kontrolne tipke: Esc, Insert, Delete i End.\n")
    print("Esc - izlaz iz programa\n")
    print("Insert - unos koeficijenata a i b linearne funkcije\n")
    print("Delete - brisanje nacrtanog prozora\n")
    print("End - snimanje slike nacrtanog grafa (grafova)\n")
    print("_______________________________________________________________\n")

# osluskivanje komandi
prozor.listen()

# u iscekivanju Godota, pardon snimanja datoteke
prozor.onkey(spremisliku, "End")

# unos nove linearne funkcije
prozor.onkey(novi_graf, "Insert")

# brisanje nacrtanih grafova
prozor.onkey(novi_prozor, "Delete")

#izlaz iz programa
prozor.onkey(izlaz, "Escape")

# ispis pomoci i crtanje radnog prozora, kks = Kartezijev koordinatni sustav
pomoc()
kks()
