#! /usr/bin/python3

#ORDINARY DIFFERENTIAL EQUATION SOLVER
from math import exp

def EulersMethod():
    print("Euler's Method")
    (x,y) = (0,0)  #initial conditions
    step = .1
    upper = .5
    while x <= upper:
        print((x,y))
        (x,y) = (x+step, y+step*(x+y))

def RungeKutta4((x,y),step,upper):
    print("RK-4")
    while x<=upper:
        k1 = (x+y)
        k2 = (x+step/2+y+step*k1/2)
        k3 = (x+step/2+y+step*k2/2)
        k4 = (x+step+y+step*k3)
        deriv = step*(k1+2*k2+2*k3+k4)/6
        (x,y) = (x+step,y+deriv)
        print((x,y))

def AdamsBashforth2((x,y),step,upper):
    print("AB-2")
    back1 = (.1,0.005)
    back2 = (x,y)
    while x<upper:
        new = (back1[0]+step,back1[1]+step/2*(3*(back1[0]+back1[1])-(back2[0]+back2[1])))
        (back1,back2) = (new,back1)    
        print(new)
        x = x+step

def AdamsMoulton2(y,h):
    print("AM-2")
    while len(y)<6:
        a = len(y)-1
        new = (y[a]+(5*h*(a+1)+8*(h*a+y[a])-h*(a-1)-y[a-1])*h/12)*12/(7*h)
        y.append(new)
    print y

def ImprovedEuler((x,y),step,upper):
    print("Improved Euler")
    while x<=upper:
        k1 = step*(x+y)
        k2 = step*(x+step/2 + y+k1/2)
        (x,y) = (x+step, y+k2)
        print((x,y))
        

def Predictor(y,a):
    h = .1
    return y[a] + (55*(h*a + y[a])-59*(h*(a-1)+y[a-1])+37*(h*(a-2)+y[a-2])-9*(h*(a-3)+y[a-3]))*h/24

def Corrector(y):
    h = .1
    while len(y) < 6:
        a = len(y)-1
        predictor = Predictor(y,a)
        value = y[a] + (9*(h*(a+1)+predictor)+19*(h*(a)+y[a])-5*(h*(a-1)+y[a-1])+h*(a-2)+y[a-2])*h/24
        y.append(value)
    print y

#y = [0, 0.005,0.021025,0.0492326]
#x = [0,.1*.1/2,.2*.2/2,.3*.3/2]
#Corrector(y)
#Corrector(x)
#ImprovedEuler((0,0),.1,.5)
#AdamsMoulton2([0,.005],.1)
#AdamsBashforth2((0,0),.1,.5)

RungeKutta4((0,0),.1,.5)

print(exp(.5)-1.5)
#EulersMethod()
