import numpy as np

class Box:
    def __init__(self, boxsize, particle_number, temperature) -> None:
        self.boxsize = boxsize
        self.particle_number = particle_number
        self.temperature = temperature
        self.particles = np.array([Particle(boxsize) for _ in range(particle_number)])
         

class Particle:
    eps = 2
    sigma = 2
    ex=np.array([1,0])
    ey=np.array([0,1])

    def __init__(self, boxsize) -> None:
        self.radius = 0.5
        self.position = np.array([(np.random.uniform(0, boxsize)),
            (np.random.uniform(0, boxsize) ) ] )
        self.velocity = np.array([(np.random.random()-1./2),
            (np.random.random()-1./2)])
        self.force_res = 0

    def force(self, r2):
        r12=((r2[0]- self.position[0])**2+(r2[1]-self.position[1])**2)**(1/2)
        x12=r2[0]-self.position[0]
        y12=r2[1]-self.position[1]
        F=(-48*self.eps/self.sigma**2)*((self.sigma/r12)**14-1/2*(self.sigma/r12)**8)*(x12*self.ex+y12*self.ey)
        return F




