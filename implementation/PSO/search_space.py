import random
import numpy as np
from particle import Particle

# Global Fixed Hyper-Parameters
W = 0.5
c1 = 0.8
c2 = 0.9

class Space():
    def __init__(self, target, target_error, n_particles):
        self.target = target
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*50, random.random()*50])
        
        # User Defined
        self.target_error = target_error
        self.n_particles = n_particles

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def fitness(self, particle):
        return particle.position[0] ** 2 + particle.position[1] ** 2 + 1
        # 

    def set_pbest(self):
        for particle in self.particles:
            fitness_candidate = self.fitness(particle)
            if(particle.pbest_value > fitness_candidate):
                particle.pbest_value = fitness_candidate
                particle.pbest_position = particle.position

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_candidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_candidate):
                self.gbest_value = best_fitness_candidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            new_velocity = (W*particle.velocity) + (c1*random.random()) * (particle.pbest_position - particle.position) + (random.random()*c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
        
