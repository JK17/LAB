import numpy as np
import math
import matplotlib.pyplot as plt 

G=0.01
M=500.0
m=0.1
dt=0.001 #krok czasowy
N=100000 #number of steps
r0=np.array([2.,0.]) #wektor polozenia poczatkowego
p0=np.array([0.,0.1]) #wektor pedu poczatkowego
T=np.linspace(0, N*dt, N) #tworze czas


#definiujemy przydatne funkcje
def force(r):
    F=(-G*M*m/(np.dot(r,r)**(3/2)))*r
    return F

def potential(r):
    V=-G*M*m/(math.sqrt(r[0]**2+r[1]**2))
    return V

def kinetic(p):
    Ek=(math.sqrt(p[0]**2+p[1]**2))**2/(2*m)
    return Ek

r=r0
p=p0
posx=[]
posy=[]
xpen=[]
ypen=[]
Ep_wykres=[potential(r0),]
Ek_wykres=[kinetic(p0),]
Ec=[]

p1=p-force(r)*0.5*dt #definiuje predkosc w -1/2dt


for i in range(0, N):
    f=force(r) #licze sile w aktualnej chwili t=0
    
    p2=p1+f*dt #licze predkosc w nastepnej polowie chwili t=dt/2
    r2=r+p2*dt/m #licze polozenie w nastepnej chwili t=dt
    Ep_wykres.append(potential(r2))
    
    posx.append(r2[0])
    posy.append(r2[1])
    xpen.append(p2[0])
    ypen.append(p2[1])
    
    p_n=0.5*(p2+p1) #licze predkosc w aktualnej chwili
    if i > 0:
        Ek_wykres.append(kinetic(p_n))
    
    p1=p2
    r=r2
    
for j in range(0,N):
    Ec.append(Ek_wykres[j]+Ep_wykres[j])
    
Ep_wykres.pop(-1)   

#plt.plot(posx,posy)
#plt.plot(T,Ep_wykres)
#plt.plot(T,Ek_wykres)
plt.plot(T,Ec)
#usuniecie if oraz linijki 62 skutkuje przesunieciem Ep wzgledem Ek