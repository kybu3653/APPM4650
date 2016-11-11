#!/bin/usr/env python

from math import exp,ceil
import matplotlib.pyplot as plt

def c(x,y):
    return x+y

def f(x,y):
    return exp(y)/3-y #fizzle data delta = 1/3

def e(x,y):
    return 1/(exp(x)-x)

def RK4(IC,h,upper,f):
    count = int(ceil(upper/h))
    est = [IC]
    for i in range(0,count):
        x = est[i][0]
        y = est[i][1]
        k1 = f(x,y)*h
        k2 = f(x+h/2,y+k1/2)*h
        k3 = f(x+h/2,y+k2/2)*h
        k4 = f(x+h,y+k3)*h
        est.append((x+h,y+(k1+2*(k2+k3)+k4)/6)) 
    #for i in range(0,len(est)):
    #    x = est[i][0]
    #    y = est[i][1]
    #    print('{',y,',',x,'},')
    return est

def fizzle(plot):
    fizzle = RK4((0,0),.1,10,f)
    if plot:
        x_fiz = [x[0] for x in fizzle]
        y_fiz = [x[1] for x in fizzle]
        plt.plot(x_fiz,y_fiz)
        plt.plot(x_fiz,y_fiz,'or')
        plt.show()

def explosion(plot):
    explosion = RK4((0,0),.1,10,e)
    if plot:
        x_exp = [x[1] for x in explosion]
        y_exp = [x[0] for x in explosion]

        plt.plot(x_exp,y_exp)
        plt.plot(x_exp,y_exp,'or')
        plt.show()

plot = int(raw_input("Plot? 1/0 "))

fizzle(plot)
explosion(plot)
#print(RK4((0,0),.1,1,c))
