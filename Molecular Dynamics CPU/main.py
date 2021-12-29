import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

from classes import Box, Particle

particleNumber=36
boxsize=40.0
temp=2.5

box = Box(boxsize, particleNumber, temp)
box.initial_velocity()

tmax = 5
t=0
dt= box.particles[0].get_dt

for t in np.arange(0, tmax, dt):
    for p_i in box.particles:
        # compute acting force on every particle
        f = 0
        for p_j in box.particles:
            if p_i != p_j:
                force = p_i.force(p_j.position)
                f += force
        p_i.force_res = f

    #compute velocity in next dt/2
    for p_i in box.particles:
        p_i.velocity_plus_dt_2()


        #compute 
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