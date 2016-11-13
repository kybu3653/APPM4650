#!/bin/usr/env python

from math import exp,ceil
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

##ROOT FINDING
def lf(y):
    return exp(y) - 3*y

def bisection(a, b, count):
    mid = (a+b)/2
    
    temp = (mid-a)/a
    if (temp > .01 or temp < -.01):
        value = lf(a)*lf(mid)
        if value > 0:
            return bisection(mid, b, count+1)
        elif value < 0:
            return bisection(a, mid, count+1)
        else:
            return mid
    return mid

##INTEGRATION
def lateExp(x):
    return 3/(exp(x)-3*x)

def SimpsonsMethod(lower,upper,step,f):
    fsum = f(lower)+f(upper)
    print fsum
    iterations = int(ceil((upper-lower)/step))
    x = step
    for i in range(1,iterations):
        if i%2 == 1: #odd
            fsum = fsum + 4*f(x)
        else:
            fsum = fsum + 2*f(x)
        x = x+step
    return step/3*fsum

def Trapezoidal(lower,upper,step,f):
    fsum = f(lower) + f(upper)
    x = step
    while x < upper:
        fsum = fsum + 2*f(x)
        x = x+step
    return 1/2*step*fsum

def GaussianQuadrature(n,g):
    if n==2:
        return g(-1/sqrt(3)) + g(1/sqrt(3))
    elif n==3:
        a = sqrt(3/5)
        return 8/9*g(0)+5/9*(g(a)+g(-a))


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
    plotrange = 16
    fizzle = RK4((0,0),.1,plotrange,f)
    theta_fizz = bisection(0.5,1,0)
    print(theta_fizz)
    if plot:
        x_fiz = [x[0] for x in fizzle]
        y_fiz = [x[1] for x in fizzle]
        plt.plot(x_fiz,y_fiz,'black')           #fit points
        plt.plot(x_fiz,y_fiz,'.',color = 'black')      #plot points
        plt.ylabel("y label")
        plt.xlabel("x label")
        plt.title("TITLE")
        x = np.arange(0, plotrange, 0.1);
        y = -.5*(np.exp(-2*x/3)-1)
        plt.plot(x, y)
        theta_fizz = theta_fizz+0*x
        plt.plot(x,theta_fizz,'--',color = "red")
        red_patch = mpatches.Patch(color='red', label='Late Fizzle')
        blue_patch = mpatches.Patch(color='blue', label='Early Fizzle')
        black_patch = mpatches.Patch(color = 'black',label='Numerical Approximation') 
        plt.legend(handles=[black_patch,blue_patch, red_patch],loc='lower right')
        plt.show()

def explosion(plot):
    explosion = RK4((0,0),.1,10,e)
    print(SimpsonsMethod(0,25,.1,lateExp))
    print(Trapezoidal(0,20,.1,lateExp))
    if plot:
        x_exp = [x[1] for x in explosion]
        y_exp = [x[0] for x in explosion]

        plt.plot(x_exp,y_exp,'black')
        plt.plot(x_exp,y_exp,'.',color='black')
        plt.ylabel("y label")
        plt.xlabel("x label")
        plt.show()

plot = int(raw_input("Plot? 1/0 "))

fizzle(plot)
#explosion(plot)
