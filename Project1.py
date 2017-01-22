#!/bin/usr/env python

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
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
    if (temp > .0001 or temp < -.0001):
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
    return 1/(exp(x)-x)

def SimpsonsMethod(lower,upper,step,f):
    fsum = f(lower)+f(upper)
    iterations = int(ceil((upper-lower)/step))
    x = step
    for i in range(1,iterations):
        if i%2 == 1: #odd
            fsum = fsum + 4*f(x)
        else:
            fsum = fsum + 2*f(x)
        x = x+step
    return step/3*fsum

def SimpsonsMethod(lower,upper,step,f):
    fsum = f(lower)+f(upper)
    iterations = int(ceil((upper-lower)/step))
    x = step
    for i in range(1,iterations):
        if i%2 == 1: #odd
            fsum = fsum + 4*f(x)
        else:
            fsum = fsum + 2*f(x)
        x = x+step
    return step/3*fsum


#ODE solving

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
    return est

def fizzle(plot,h,upper):
    theta_fizz = bisection(.5,1,0)
    fizzle = RK4((0,0),h,upper,f)
    if plot:
        x_fiz = [x[0] for x in fizzle]
        y_fiz = [x[1] for x in fizzle]
        plt.plot(x_fiz,y_fiz,'black')           
#        plt.plot(x_fiz,y_fiz,'.',color = 'black')      
        #plt.xlabel("sigma")
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.xlabel(r'$\sigma$', size = 20)
        plt.ylabel(r"$\theta$",size = 20)
        plt.title( r"Fizzle ($\delta = 1/3$)",size = 20)
        x = np.arange(0, 1, h)
        y = -.5*(np.exp(-2*x/3)-1)
        plt.plot(x, y)
        x1 = np.arange(11,upper,h)
        theta_fizz = theta_fizz+0*x1
        plt.plot(x1,theta_fizz,color = "red")
        red_patch = mpatches.Patch(color='red', label='Late Fizzle')
        blue_patch = mpatches.Patch(color='blue', label='Early Fizzle')
        black_patch = mpatches.Patch(color = 'black',label='Numerical Approximation') 
        plt.legend(handles=[black_patch,blue_patch, red_patch],loc='lower right',fontsize=13)
        plt.show()

def explosion(plot,h,upper):
    explosion = RK4((0,0),h,upper,e)
    sigma_exp = SimpsonsMethod(0,15,h,lateExp)
    if plot:
        x_exp = [x[1] for x in explosion]
        y_exp = [x[0] for x in explosion]
        plt.title(r"Explosion ($\delta = 1$)",size = 20)
        x = np.arange(1.3, upper, h)
        y = sigma_exp-1/np.exp(x)
        x1 = np.arange(0,.7,h) 
        plt.plot(x1,x1,color = 'blue') #early explosion
        plt.plot(y,x,color = 'red')  #late explosion
        plt.plot(x_exp,y_exp,'black')  #numerical approx
#        plt.plot(x_exp,y_exp,'.',color='black')
        plt.ylabel(r"$\theta$",size = 20)
        plt.xlabel(r"$\sigma$",size = 20)
        red_patch = mpatches.Patch(color='red', label='Late Explosion')
        blue_patch = mpatches.Patch(color='blue', label='Early Explosion')
        black_patch = mpatches.Patch(color = 'black',label='Numerical Approximation') 
        plt.legend(handles=[black_patch,blue_patch, red_patch],loc=2,fontsize = 13)
        plt.show()

plot = 1#int(raw_input("Plot? 1/0 "))
step_size = .01#float(raw_input("Step Size? "))
upper_bound = 15#int(raw_input("Upper Bound? "))
fizzle(plot,step_size,upper_bound)
explosion(plot,step_size,upper_bound)
