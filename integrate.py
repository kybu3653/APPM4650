#! /usr/bin/python3

from math import exp,ceil,sqrt

def f(x):
    return pow(x,2)*exp(-pow(x,2))

def CompositeMidpoint(lower,upper,step):
    iterations = ceil((upper-lower)/step)
    fsum = 0
    for i in range(1,iterations+1):
        x_val = lower+(i-1/2)*step
        fsum = fsum + f(x_val)
    return step*fsum

def TrapezoidalMethod(lower,upper,step):
    fsum = f(lower) + f(upper)
    x = step
    while x < upper:
        fsum = fsum + 2*f(x)
        x = x+step
    return 1/2*step*fsum

def SimpsonsMethod(lower,upper,step):
    fsum = f(lower)+f(upper)
    iterations = ceil((upper-lower)/step)
    x = step
    for i in range(1,iterations):
        if i%2 == 1: #odd
            fsum = fsum + 4*f(x)
        else:
            fsum = fsum + 2*f(x)
        x = x+step
    return step/3*fsum

def g(t):
    x= (t+1)/2
    return 1/2*pow(x,2)*exp(-x)
    

def GaussianQuadrature(n):
    if n==2:
        return g(-1/sqrt(3)) + g(1/sqrt(3))
    elif n==3:
        a = sqrt(3/5)
        return 8/9*g(0)+5/9*(g(a)+g(-a))

print("Composite Method: ",CompositeMidpoint(0,2,.25))
print("Trapezoidal Method: ",TrapezoidalMethod(0,2,.25))
print("Simpson's 1/3 Rule: ", SimpsonsMethod(0,2,.25))
print("Gaussian Quadrature n=2", GaussianQuadrature(2))
print("Gaussian Quadrature n=3", GaussianQuadrature(3))
