import matplotlib.pyplot as plt
import math
import numpy as np
import random

#QUESTIONS TO ASK
#Is connector the distance between amino acid pairs, which we would use to sum the distances
#All interactions vs spring interactions
#spring force vs LJ force
#where do we return vector coordinates

#################################################################
def Polymer_MD_Python():
    # initialize parameters
    #use N= 25, 10, 5
    N = 25 #no. of particles
    T = 0.05 #temperature
    dt = 0.0005 #integration time step
    steps = 500000 #time steps

    step_gyration = 200000

    epsilon_LJ = 1
    cutff_LJ = 2.5
    spring_coeff = 5
    min_sep = 1.122 #r_0

    L = min_sep*N
    print_interval = 1000
####################################################################
    #initialize x coordinates
    x = initial_configuration(min_sep, N)
    #print(x)
    #pairs will be populated
    pairs = []
#####################################################################
    #main loop

    
    # for step_i in range(0, steps): #molecular dynamics loop
    #     x, pairs = steepest_descent(N, x, dt, cutff_LJ, epsilon_LJ, min_sep, spring_coeff, T)
    #     #print(pairs)
    #     if (np.mod(step_i-1,print_interval) == 0):  #print every 1000 steps
    #         mytitle = ["step=",str(step_i), "N=", str(N), "L=", str(L)]
    #         print(mytitle)
    #         #we need pairs
    #         visualize_particles(N, x, L, pairs, mytitle)


############################# PART 1 ##############################
    # lengths = [25,10,5]
    # arrays = [[],[], []]
    # for index, len in enumerate(lengths):
    #     x = initial_configuration(min_sep, len)
    #     for step_i in range(0, step_gyration): #molecular dynamics loop
    #         #motion - position of next time step
    #         x, pairs = steepest_descent(len, x, dt, cutff_LJ, epsilon_LJ, min_sep, spring_coeff, T)
    #         #returns a size
            
    #         if (np.mod(step_i-1,print_interval) == 0):  #print every 1000 steps
    #             arrays[index].append(radius_gyration_size(len, x))
            
        
    #             mytitle = ["Radius of Gyration",  "Chain Lengths =25, 10, 5", "step=", str(step_i)]
                
    #             print(mytitle)
    # visualize_size(N, arrays[0], arrays[1], arrays[2],  pairs, mytitle)


            
#PART 2 - LJ forces
    epsilon_LJ=[1, 0.5, 0]
    radius = [[],[],[]]
    for index, e in enumerate(epsilon_LJ):
        x = initial_configuration(min_sep, N)
        for step_i in range(0, step_gyration): #molecular dynamics loop
            #motion - position of next time step
            x, pairs = steepest_descent(N, x, dt, cutff_LJ, e, min_sep, spring_coeff, T)
            #returns a size
            
            if (np.mod(step_i-1,print_interval) == 0):  #print every 1000 steps
                radius[index].append(radius_gyration_size(N, x))
               
        
        
                mytitle = ["Radius of Gyration",  "potential strengths =1, 0.5, 0", "step=", str(step_i)]
                
                print(mytitle)
                #we need pairs
                #visualize size over 200000 time steps for sizes 25,10,5
        
   
    visualize_lj(N, radius[0], radius[1], radius[2],pairs, mytitle)


# Initial coordinates of every amino acid.
def initial_configuration(initial_min_sep, N):
    x = np.zeros((N, 2))
    for i in range(0,N):
        x[i][0] = initial_min_sep*i - (initial_min_sep*N/2)
    return x


def steepest_descent(N,x,dt, cutoff_LJ,epsilon_LJ,min_sep,spring_coeff,T):
    F_particles,_,pairs = forces(N,x,cutoff_LJ,epsilon_LJ,min_sep,spring_coeff)
    F = F_particles
    x = x + (dt * F) + np.dot(T, (np.random.rand(x.shape[0], x.shape[1]) - 0.5))
    return x, pairs


#this may be useful for radius of gyration
def all_interactions(N,x,cutoff): #obtain interacting pairs
    ip =0
    connector = []
    pair = []
    for i in range(0, N-1):
        for j in range(i+1, N):
            distance = x[j,:]-x[i,:]  # distance : (1x2)

            if np.linalg.norm(distance) < cutoff:
                ip = ip + 1
                #appending pairs of amino acids
                pair.append([i,j])
                connector.append([distance])
    return ip, pair, connector

#Obtain interacting pairs
def spring_interactions(N,x):
    ip = 0
    connector = []
    pair = []
    for i in range(0, N-1):
        j = i+1
        distance = x[j,:]-x[i,:]
        ip += 1
        pair.append([i,j])
        connector.append([distance])
    return ip, pair, connector

def forces(N,x,cutoff_LJ,epsilon_LJ,min_sep,spring_coeff):
    #what is P?
    F = np.zeros((N,2))
    P = np.zeros((N,2))
    # LJ Forces
    no, pair, connector = all_interactions(N,x,cutoff_LJ) #interacting pairs
    for i in range(0, no):
        FORCE = force_LJ(connector[i], epsilon_LJ)
        F[pair[i][0]] = F[pair[i][0]]-FORCE
        F[pair[i][1]]=F[pair[i][1]]+FORCE #action = reaction
        P[pair[i][0]]=P[pair[i] [0]]+(np.sum(FORCE* connector[i], axis=0))
        P[pair[i][1]]=P[pair[i][1]]+(np.sum(FORCE* connector[i], axis=0))

    #Spring Forces
    no, pair, connector = spring_interactions(N, x) #interacting pairs
    for i in range(0,no):
        #print(f"connector at i: {connector[i]}")
        FORCE = force_springs(connector[i], spring_coeff, min_sep)
        F[pair[i][0]]=F[pair[i][0]]-FORCE
        F[pair[i][1]]=F[pair[i][1]]+FORCE # action = reaction;
        P[pair[i][0]]=P[pair[i][0]]+(np.sum(FORCE* connector[i], axis=0))
        P[pair[i][1]]=P[pair[i][1]]+(np.sum(FORCE* connector[i], axis=0))
    return F, P, pair

def force_springs(r_vector,spring_coeff_array,min_sep):
    #y axis
    r2 = np.sum(np.square(r_vector), axis = 1)

    #this is the positions to plot
    r = np.sqrt(r2)
    #print(len(r))
    #print(f"r:{r}")
    curr_force = np.zeros((len(r2),2))
    val_1 = np.multiply(np.subtract(r,min_sep), (np.divide(r_vector[0][0], r)), out=None)
    val_2 = np.multiply(np.subtract(r,min_sep), (np.divide(r_vector[0][1], r)), out=None)
    curr_force[0][0] = np.multiply(np.transpose(-spring_coeff_array), val_1 )
    curr_force[0][1] = np.multiply(np.transpose(-spring_coeff_array), val_2)
    return curr_force

def force_LJ(r_vector, epsilon_LJ):
    r = np.linalg.norm(r_vector)
    force_LJ = 24*epsilon_LJ*np.dot((np.dot(2,r**(-14))-r**(-8)),r_vector)
    return force_LJ

def visualize_particles(N, x, L, pairs, mytitle):
    X = [i[0] for i in x]
    Y = [i[1] for i in x]
    colors = (0,0,0)
    plt.ylim(top=10,bottom=-10)
    plt.xlim([-10,10])
    plt.scatter(X, Y, c=colors, alpha=0.5)
    plt.title(mytitle)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return

def visualize_size(N, size_25, size_10, size_5, pairs, mytitle):

    plt.ylim(top=80,bottom=0)
    plt.plot(size_25, color = 'blue', alpha=0.5, label = "N=25")
    plt.plot(size_10, color = 'green', alpha=0.5, label = "N=10")
    plt.plot(size_5, color='red', alpha=0.5, label = "N = 5")
    plt.title(mytitle)
    plt.xlabel("Time")
    plt.ylabel("Size")
    plt.show()
    return

def visualize_lj(N, lj1, lj2, lj3 ,pairs, mytitle):

    plt.ylim(top=80,bottom=0)
    plt.plot(lj1, color = 'blue', alpha=0.5, label = "Potential strength=1")
    plt.plot(lj2, color = 'green', alpha=0.5, label = "Potential strength=0.5")
    plt.plot(lj3, color = 'red', alpha=0.5, label = "Potential strength=0")
    # print("One")
    # plt.plot(lj_half, color = 'green', alpha=0.5, label = "Potential strength=1")
    # print("Half")
    # plt.plot(lj_0, color = 'red', alpha=0.5, label = "Potential strength=1")
    # print("Zero")
    #plt.plot(lj_half, color = 'green', alpha=0.5, label = "Potential strength=0.5")
    #plt.plot(lj_0, color = 'red', alpha=0.5, label = "Potential strength=0")
    plt.title(mytitle)
    plt.xlabel("Time")
    plt.ylabel("Size")
    plt.show()
    return


##########Radius of Gyration Implementation####################

#every step of the simulation should return a size as the protein folds
def radius_gyration_size(N, x):

   #25 x,y coordinates for each instance of the simulation: 200000/1000 simulations
    sum = 0
 
    for i in range(N):
        for j in range(N):
            if i!=j:
                #summing distance between amino acid i and j with distance formula
                #(ri - rj)^2
                #x[i,:]
                diff = x[i,:] - x[j,:]
                #print(f"diff: {diff}")
                sum += (diff[0] - diff[1])**2


    return sum/(2* (N**2))


Polymer_MD_Python()






   #simulation for radius of gyration -  part 1
    # size_25 = []
    # size_10 = []
    # size_5 = []
    # step_axis = []
    # for step_i in range(0, step_gyration): #molecular dynamics loop
    #     #motion - position of next time step
    #     x, pairs = steepest_descent(N, x, dt, cutff_LJ, epsilon_LJ, min_sep, spring_coeff, T)
    #     #returns a size
        
        
    #     if (np.mod(step_i-1,print_interval) == 0):  #print every 1000 steps
    #         size_25.append(radius_gyration_size(25, x))
    #         size_10.append(radius_gyration_size(10, x))
    #         size_5.append(radius_gyration_size(5, x))
    #         step_axis.append(step_i)
    #         mytitle = ["Radius of Gyration",  "N= 25,10,5", "step=", str(step_i)]
            
    #         print(mytitle)
    #         #we need pairs
    #         #visualize size over 200000 time steps for sizes 25,10,5
    
    # visualize_size(N, size_25, size_10, size_5,  pairs, mytitle)