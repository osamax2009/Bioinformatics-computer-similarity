# import packages
#probability of being in each state after 50 
#steps with a starting distribution of {1,0,0}



import numpy as np
transition_matrix =  np.array([[0, 0.5, 0.5],
                               [0.4, 0.3, 0.3],
                               [0.6, 0.2, 0.2]])# set initial distribution
initial_dist = np.array([1,0,0])# simulate 50 time steps
for _ in range(50):
    update = initial_dist @ transition_matrix
    initial_dist = update
    
print(initial_dist)