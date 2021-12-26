import numpy as np

class Box:
    def __init__(self, boxsize, particle_number, temperature) -> None:
        self.boxsize = boxsize
        self.particle_number = particle_number
        self.temperature = temperature
        self.particles = np.array([Particle(boxsize) for _ in range(particle_number)])
         

class Particle:

    def __init__(self, boxsize) -> None:
        self.radius = 0.5
        self.position = np.array([(np.random.uniform(0, boxsize)),
            (np.random.uniform(0, boxsize) ) ] )
        self.velocity = np.array([(np.random.random()-1./2),
            (np.random.random()-1./2)])

b = Box(40.0, 10, 2.5)


