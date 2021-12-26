import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

from classes import Box, Particle

particleNumber=36
boxsize=40.0
temp=2.5

box = Box(boxsize, particleNumber, temp)



#rysowanie poczatkowego polozenia czastek
plt.clf()
F=plt.gcf()
for p in box.particles:
    a=plt.gca()
    cir=Circle((p.position[0],p.position[1]), radius=p.radius)
    a.add_patch(cir)
    plt.plot()
plt.xlim((0,boxsize))
plt.ylim((0,boxsize))
F.set_size_inches((6,6))
plt.show()