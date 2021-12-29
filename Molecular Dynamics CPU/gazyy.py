#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:57:56 2020

@author: jk406073
"""

import numpy as np
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class czastka:
    def __init__(self, promien, pos, vel,sila):
        self.promien=promien
        self.r=pos
        self.v=vel
        self.f=sila

def force(r1,r2):
    r12=((r2[0]-r1[0])**2+(r2[1]-r1[1])**2)**(1/2)
    x12=r2[0]-r1[0]
    y12=r2[1]-r1[1]
    F=(-48*eps/sigma**2)*((sigma/r12)**14-1/2*(sigma/r12)**8)*(x12*ex+y12*ey)
    return F


#stale
particleNumber=36
boxsize=40.0
b=boxsize
eps=1.0
sigma=1.0
promien=0.5
dt=0.001
temp=2.5
delta=2
nx=6
ny=6       
tmax=5
ex=np.array([1,0])
ey=np.array([0,1])
m=1

particles=[]
for i in range(nx):
    for j in range(ny):
        polozenie=np.array([i*delta+0.1, j*delta+0.1])
        predkosc=np.array([(random.random()-1./2),(random.random()-1./2)])
        sila=0
        particles.append(czastka(promien,polozenie,predkosc,sila))
        
sumv=0.0
sumv2=0.0
for p in particles:
    sumv=sumv+p.v
sumv=sumv/particleNumber
for p in particles:
    p.v=(p.v-sumv)
for p in particles:
    sumv2=sumv2+np.dot(p.v,p.v)/2.0
sumv2=sumv2/particleNumber
fs=math.sqrt(temp/sumv2)
for p in particles:
    p.v=p.v*fs    
    
t=0
en=0

while t<tmax:    
    for p in particles:
        #p.r=p.r+p.v *dt
        #licze najpierw siły działające na p cząstke od reszty czastek
        f=0
        for j in particles:
            if p != j:
                sila=force(p.r,j.r)
                f=sila+f
                p.f=f
    for p in particles:
        p.v=p.v+p.f/m*dt
        p.r=p.r+p.v*dt
        
        if p.r[0]>b:
            p.r[0] -=b
        if p.r[0] <0:
            p.r[0] +=b
        if p.r[1]>b:
            p.r[1] -=b
        if p.r[1] <0:
            p.r[1] +=b
        #rysowanie
    if (en%100==0):
        plt.clf()
        F=plt.gcf()
        for i in range(particleNumber):
            p=particles[i]
            a=plt.gca()
            cir=Circle((p.r[0],p.r[1]), radius=p.promien)
            a.add_patch(cir)
            plt.plot()
        plt.xlim((0,boxsize))
        plt.ylim((0,boxsize))
        F.set_size_inches((6,6))
        nStr=str(en)
        nStr=nStr.rjust(5,'0')
        plt.title("Symulacja gazu Lennarda-Jonesa, krok " + nStr)
        plt.savefig('img'+nStr+'.png')
        plt.show()
        print("zapisane", nStr)
    
    t=t+dt
    en=1+en

for p in particles:
    p.v=-p.v
t=0

while t<tmax:    
    for p in particles:
        #p.r=p.r+p.v *dt
        #licze najpierw siły działające na p cząstke od reszty czastek
        f=0
        for j in particles:
            if p != j:
                sila=force(p.r,j.r)
                f=sila+f
                p.f=f
    for p in particles:
        p.v=p.v+p.f/m*dt
        p.r=p.r+p.v*dt
        
        if p.r[0]>b:
            p.r[0] -=b
        if p.r[0] <0:
            p.r[0] +=b
        if p.r[1]>b:
            p.r[1] -=b
        if p.r[1] <0:
            p.r[1] +=b
        #rysowanie
    if (en%100==0):
        plt.clf()
        F=plt.gcf()
        for i in range(particleNumber):
            p=particles[i]
            a=plt.gca()
            cir=Circle((p.r[0],p.r[1]), radius=p.promien)
            a.add_patch(cir)
            plt.plot()
        plt.xlim((0,boxsize))
        plt.ylim((0,boxsize))
        F.set_size_inches((6,6))
        nStr=str(en)
        nStr=nStr.rjust(5,'0')
        plt.title("Symulacja gazu Lennarda-Jonesa, krok " + nStr)
        plt.savefig('img'+nStr+'.png')
        plt.show()
        print("zapisane", nStr)
    
    t=t+dt
    en=1+en
    
    
    
    
    