#! /usr/bin/python3

from math import exp

def f1(t,w1,w2):
    return 3*w1+2*w2-(2*pow(t,2)+1)*exp(2*t)

def f2(t,w1,w2):
    return 4*w1+w2+(pow(t,2)+2*t-4)*exp(2*t)

def RK4(h,w10,w20,t0):
    u1 = [w10]
    u2 = [w20]
    for i in range(0,6):
        k11 = f1(t0,w10,w20)
        k12 = f2(t0,w10,w20)
        k21 = f1(t0+h/2,w10+h*k11/2,w20+h*k12/2)
        k22 = f2(t0+h/2,w10+h*k11/2,w20+h*k12/2)
        k31 = f1(t0+h/2,w10+h*k21/2,w20+h*k22/2)
        k32 = f2(t0+h/2,w10+h*k21/2,w20+h*k22/2)
        k41 = f1(t0+h,w10+h*k31,w20+h*k32)
        k42 = f2(t0+h,w10+h*k31,w20+h*k32)

        w10 = w10+h*(k11+2*(k21+k31)+k41)/6
        w20 = w20+h*(k12+2*(k22+k32)+k42)/6
        t0=t0+h
        u1.append(w10)
        u2.append(w20)
        print(w10,w20)

RK4(.2,1,1,0)
