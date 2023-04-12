#!/usr/bin/python3

import plotext as plt
import os
import datetime

def graf(a, b, c, d):
    x = range(-100,101,1)
    y = [a * xi**3 + b*xi**2 + c*xi +d for xi in x]
    return x, y

def main():
    koeficijenti = []
    i=0
    filename_txt = "graf-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filename_html = "graf-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".html"
    file_path_txt = os.path.join(os.getcwd(), filename_txt)
    file_path_html = os.path.join(os.getcwd(), filename_html)
    while True:
        print("Graf funkcije y = a*x**3 + b*x**2 + c*x + d")
        try:
            a = float(input("Unesi koeficijent a = "))
            b = float(input("Unesi koeficijent b = "))
            c = float(input("Unesi koeficijent c = "))
            d = float(input("Unesi koeficijent d = "))
            koeficijenti.append((a,b,c,d))
        except ValueError:
            print("Pogrešan unos, ponovi!")
            continue
        i=i+1
        x, y = graf(a, b, c, d)
        plt.plot(x, y, label = koeficijenti[i-1])
        plt.title("Graf funkcije y = a * x^3 + b * x^2 +c * x + d")
        plt.xlim(-100,100)
        plt.ylim(-50,50)
        plt.vline(0)
        plt.hline(0)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
        plt.save_fig(file_path_txt)
        plt.save_fig(file_path_html)
        print(koeficijenti)
        if input("Pritisni ESC za izlazak!") == chr(27):
            break

if __name__ == "__main__":
    main()
