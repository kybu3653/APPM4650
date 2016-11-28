#! /usr/bin/env python

import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def f1(y,n):              #y1'
    return y[1]

def f2(y,n):              #y2'
    return y[2]

def f3(y,n):                  #y3'
    return -1*(y[0]*y[2])/2

def f4(n):                  #F'(n)
    return F[1][n][1]

def g1(y,n):                   #y4'
    return y[1]
def g2(y,n):                   #y5'
    return -1*PR*f4(n)*y[1]

def RK4(h,upper,IC,f,n):
    length = len(IC)
    retList = [[(n,IC[x])] for x in range(length)]
    k = [[0 for x in range(4)]for y in range(length)]
    ICtemp = IC
    iterations = int(math.ceil((upper-n)/h))
    for index in range(iterations):
        for j in range(4):
            for i in range(length):
                k[i][j] = f[i](IC,index)
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

def makePlot(f,title,legend):
    colors = ["red","blue","purple","cyan"]
    patches = []
    for i in range(len(f)):
        x = [element[0] for element in f[i]]
        y = [element[1] for element in f[i]]
        plt.plot(x,y,color = colors[i]) 
        patch = mpatches.Patch(color = colors[i],label = legend[i])
        patches.append(patch)
    plt.legend(handles=patches)
    plt.title(title,size = 20)
    plt.show()

f = [f1,f2,f3]
val = .30346 #float(raw_input("F''? "))
F = RK4(.1,10,[0,0,val],f,0)
length = len(F[1])
#print F[1][len(F[1])-1]

g = [g1,g2]
#g_prime1 = float(raw_input("G'? "))
Prandtl = [.2,1,4,8]
g_prime = [-.14537,-.3909,-.73844,-.978535]
plott = []
legend = []
for i in range(len(Prandtl)):
    PR = Prandtl[i]
    legend.append(str(PR))
    G = RK4(.1,10,[1,g_prime[i]],g,0)
    #print G[0][len(G[0])-1]
    plott.append(G[0])
makePlot(plott,"G(X)",legend)
plot = 0 #int(raw_input("Plot? "))
if plot == 1:
    makePlot([F[0]],"F(X)")
    makePlot([F[1]],"F'(X)")
    makePlot([F[2]],"F''(X)")
