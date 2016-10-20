#! /usr/bin/python3

from math import exp,ceil 

def f(x):
    return pow(x,2)*exp(-pow(x,2))

def CompositeMidpoint(lower,upper,step):
    iterations = ceil((upper-lower)/step)
    fsum = 0
    for i in range(1,iterations+1):
        x_val = lower+(i-1/2)*step
        fsum = fsum + f(x_val)
    return step*fsum

composite = CompositeMidpoint(0,2,.25)
print(composite)
