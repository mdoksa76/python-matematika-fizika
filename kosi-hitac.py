#!/usr/bin/python3

import plotext as plt
import os
import datetime
import math

px = []
py = []
v0alfa = []
maxx = []
maxy = []

def kosihitac(v0, alfa):
    t=0
    x=0
    y=0
    px.append(x)
    py.append(y)
    dt=0.01
    g=9.81
    vx = v0 * math.cos(alfa * math.pi/180)
    vy = v0 * math.sin(alfa * math.pi/180)
    while (y>=0):
        t = t + dt
        x = vx * t
        vy = vy - g * dt
        y = y + vy * dt
        px.append(x)
        py.append(y)
        maxx.append(max(px))
        maxy.append(max(py))

def main():
    i=0
    filename_txt = "kosi-hitac-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filename_html = "kosi-hitac-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".html"
    file_path_txt = os.path.join(os.getcwd(), filename_txt)
    file_path_html = os.path.join(os.getcwd(), filename_html)
    while True:
        try:
            v0 = float(input("početna brzina hica = "))
            alfa = float(input("kut hica = "))
            v0alfa.append((v0, alfa))
        except ValueError:
            print("Pogrešan unos, ponovi!")
            continue
        i=i+1
        kosihitac(v0, alfa)
        print("Kosi hitac")
        plt.scatter(px, py, label = v0alfa[i-1])
        plt.xlim(0, max(maxx))
        plt.ylim(0, max(maxy))
        plt.hline(0)
        print(px, py)
        plt.title("Kosi hitac")
        plt.xlabel("x - domet hica")
        plt.ylabel("y - visina hica")
        plt.show()
        plt.save_fig(file_path_txt)
        plt.save_fig(file_path_html)
        px.clear()
        py.clear()
        if input("Pritisni ESC za izlazak, ENTER za novi unos!") == chr(27):
            break

if __name__ == "__main__":
    main()
