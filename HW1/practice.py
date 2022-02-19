import numpy as np

#particles along x axis via step
def initial_configuration(initial_min_sep, N):
    x = np.zeros((N, 2))
    for i in range(0,N):
        x[i][0] = initial_min_sep*i - (initial_min_sep*N/2)
    print(x)
    return x

  # initialize parameters
    #use N= 25, 10, 5
N = 25 #no. of particles
T = 0.05 #temperature
dt = 0.0005 #integration time step
steps = 500000 #time steps

epsilon_LJ = 1
cutff_LJ = 2.5
spring_coeff = 5
min_sep = 1.122 #r_0

L = min_sep*N
print_interval = 1000
####################################################################
#initialize x coordinates
x =  initial_configuration(min_sep, N)
pairs = []

