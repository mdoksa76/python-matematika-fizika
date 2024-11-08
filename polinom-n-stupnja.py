#!/usr/bin/python3

import plotext

koeficijenti_list=[[1,0],[-0.5,-5],[0.1,0,-30],[9],[0.001,0,0,25]]
T=[]
global_min_y=float('inf')
global_max_y=float('-inf')

def tocke(koeficijenti, tx=(-50, 50)):
  for x in range(tx[0], tx[1]+1):
  y=sum(k*x**i for i, k in enumerate(reversed(koeficijenti)))
  y=round(y, 2)
  T.append((x, y))
  return T

for koeficijenti in koeficijenti_list:
  T=tocke(koeficijenti)
  y_oni=[t[1] for t in T]
  global_min_y=min(global_min_y, min(y_oni))
  global_max_y=max(global_max_y, max(y_oni))
  T.clear()

def graf(koeficijenti):
  T=tocke(koeficijenti)
  print(T)
  kx=[t[0] for t in T]
  ky=[t[1] for t in T]
  plotext.theme("pro")
  plotext.scatter(kx, ky, marker="•", label=koeficijenti)
  plotext.title("Polinom n-tog stupnja - plotext plot!")
  plotext.xlabel("x")
  plotext.ylabel("y")
  plotext.hline(0)
  plotext.vline(0)
  plotext.show()

  T.clear()

for koeficijenti in koeficijenti_list:
  graf(koeficijenti)
