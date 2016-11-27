#! /usr/bin/env python

import math
import matplotlib.pyplot as plt

def f1(y):
    return y[1]

def f2(y):
    return y[2]

def f3(y):
    return -1*(y[0]*y[2])/2

def RK4(h,upper,IC,f,n):
    length = len(IC)
    retList = [[(n,IC[x])] for x in range(length)]
    k = [[0 for x in range(4)]for y in range(length)]
    ICtemp = IC
    iterations = int(math.ceil((upper-n)/h))
    for index in range(iterations):
        for j in range(4):
            for i in range(length):
                k[i][j] = f[i](IC)
            if j == 3:
                mult = 1
            else:
                mult = 2
            for x in range(length):
                IC[x] = IC[x]+h*k[x][j]/mult
        n+=h
        for i in range(length):
            IC[i] +=  h*(k[i][0] + 2*(k[i][1]+k[i][2])+k[i][3])/6
            retList[i].append((n,IC[i]))
            
    return retList


def makePlot(f):
    x = [element[0] for element in f]
    y = [element[1] for element in f]
    plt.plot(x,y)
    plt.show()

f = [f1,f2,f3]
val = .30346 #float(raw_input("F''? "))
F = RK4(.1,10,[0,0,val],f,0)
length = len(F[1])

print F[1][length-1]
makePlot(F[1])
