# User Defined Hyper-Parameters
n_iterations = int(input("Inform the number of iterations: "))
target_error = float(input("Inform the target error : "))
n_particles = int(input("Inform the number of particles: "))

from particle import Particle
from search_space import Space

searchspace = Space(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(searchspace.n_particles)]
searchspace.particles = particles_vector
searchspace.print_particles()

iteration = 0
while(iteration < n_iterations):
    searchspace.set_pbest()    
    searchspace.set_gbest()

    if(abs(searchspace.gbest_value - searchspace.target) <= searchspace.target_error):
        break

    searchspace.move_particles()
    iteration += 1
    
print("The best solution is: ", searchspace.gbest_position, " in n_iterations: ", iteration)
