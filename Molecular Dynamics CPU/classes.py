import numpy as np

class Box:
    def __init__(self, boxsize, particle_number, temperature) -> None:
        self.boxsize = boxsize
        self.particle_number = particle_number
        self.temperature = temperature
        self.particles = np.array([Particle(boxsize, mass=1) for _ in range(particle_number)])
    
    def initial_velocity(self):
        sumv = 0
        sumv2 = 0
        for p in self.particles:
            sumv += p.velocity
        sumv=sumv/self.particle_number # center mass velocity
        for p in self.particles:
            p.velocity = p.velocity - sumv #mass center at rest
            sumv2 = sumv2 + np.dot(p.velocity, p.velocity) / 2.0 
        sumv2=sumv2/self.particle_number #average kinetic energy (unitary mass)
        fs=np.sqrt(self.temperature / sumv2) #scaling factor
        for p in self.particles:
            p.velocity = p.velocity * fs

class Particle:
    eps = 2
    sigma = 2
    ex=np.array([1,0])
    ey=np.array([0,1])
    dt = 0.001

    def __init__(self, boxsize, mass) -> None:
        self.mass = mass
        self.radius = 0.5
        self.position = np.array([(np.random.uniform(0, boxsize)),
            (np.random.uniform(0, boxsize) ) ] )
        self.velocity = np.array([(np.random.random()-1./2),
            (np.random.random()-1./2)])
        self.force_res = 0

    def get_dt(self):
        return self.dt

    def force(self, r2, boxsize):
        #the nearest image implementation
        r_vect = r2 - self.position
        if r_vect[0] > (boxsize/2):
            r_vect[0] = r_vect[0] - boxsize
        elif r_vect[0] < (-boxsize/2):
            r_vect[0] = r_vect[0] + boxsize

        if r_vect[1] > (boxsize/2):
            r_vect[1] = r_vect[1] - boxsize
        elif r_vect[1] < (-boxsize/2):
            r_vect[1] = r_vect[1] + boxsize

        r12 = (r_vect[0]**2 + r_vect[1]**2)**(1/2)
        #r12=((r2[0]- self.position[0])**2+(r2[1]-self.position[1])**2)**(1/2)
        #x12=r2[0]-self.position[0]
        #y12=r2[1]-self.position[1]
        x12=r_vect[0]
        y12=r_vect[1]
        F=(-48*self.eps/self.sigma**2)*((self.sigma/r12)**14-1/2*(self.sigma/r12)**8)*(x12*self.ex+y12*self.ey)
        return F
    
    def velocity_plus_dt_2(self):
        self.velocity = self.velocity + self.force_res / self.mass * self.dt

    def move_particle(self, boxsize):
        self.position = self.position + self.velocity * self.dt
        
        self.position = self.position % boxsize




