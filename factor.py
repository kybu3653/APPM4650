#!/usr/bin/python3
import math

x = [8.1,8.3,8.6,8.7]
y = [16.94410,17.56492,18.50515,18.82091]   
a = 8.4

p = 1
q = 2
val = (a-x[p])/(x[q]-x[p])*y[q]+(a-x[q])/(x[p]-x[q])*y[p]

print val
