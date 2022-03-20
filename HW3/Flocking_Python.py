###########################################################################

# March 2019, Orit Peleg, orit.peleg@colorado.edu

# Code for HW3 CSCI 4314/5314 Dynamic Models in Biology

###########################################################################



import numpy as np

import math

import matplotlib.pyplot as plt



class flock():



    def flocking_python(self):

        N = 400 #No. of Boids

        frames = 100 #No. of frames

        limit = 100 #Axis Limits

        L  = limit*2

        P = 10 #Spread of initial position (gaussian)

        V = 10 #Spread of initial velocity (gaussian)

        delta = 1 #Time Step

        c1 = 0.00001 #Attraction Scaling factor

        c2 = 0.01 #Repulsion scaling factor

        c3 = 1 #Heading scaling factor

        c4 = 0.01 #Randomness scaling factor

        vlimit = 1 #Maximum velocity

        #defining array of positions and velocities
        p_plot = []
        v_plot=[]



        #Initialize

        p = P*np.random.randn(2,N)


        v = V*np.random.randn(2,N)

        #print(v)


        #Initializing plot

        plt.ion()

        fig = plt.figure()

        ax = fig.add_subplot(111)





        for i in range(0, 10):

            v1 = np.zeros((2,N))

            v2 = np.zeros((2,N))

            #v4 = np.zeros((2,N)) #add this **********?
     

            #YOUR CODE HERE

            #Calculate Average Velocity v3 
            v3 = [np.sum(v[0, :])/N , np.sum(v[1, :])/N]*c3
            



            if (np.linalg.norm(v3) > vlimit): #limit maximum velocity

                v3 = v3*vlimit/np.linalg.norm(v3) #normalizing



            for n in range(0, N):

                for m in range(0, N):

                    if m!=n:

                        #YOUR CODE HERE

                        #Compute vector r from one agent to the next
                        r = p[: ,m] - p[: ,n]



                        if r[0] > L/2:

                            r[0] = r[0]-L

                        elif r[0] < -L/2:

                            r[0] = r[0]+L



                        if r[1] > L/2:

                            r[1] = r[1]-L

                        elif r[1] < -L/2:

                            r[1] = r[1]+L



                        #YOUR CODE HERE

                        #Compute distance between agents rmag
                        rmag = np.sqrt( r[0]**2+ r[1]**2 )
                        #Compute attraction v1
                        v1[: ,n] = v1[: ,n] +c1*r
                        #Compute Repulsion [non-linear scaling] v2
                        v2[: ,n] = v2[: ,n] -(c2*r)/rmag**2

                #YOUR CODE HERE

                #Compute random velocity component v4 - initialize????
                v4 = c4*np.random.randn(2,N)

                #print(v3)
                #Update velocity
                v[ : , n ] = v1[ : , n] + v2[ : , n]+ v3 + v4[ : , n ]
                v_plot.append(v)
            #print("v4:")
            #print(v4)

               

            #YOUR CODE HERE

            #Update position
            #this is the position for each frame
            p = p + v* delta



            #Periodic boundary

            tmp_p = p



            tmp_p[0, p[0,:]>L/2] = tmp_p[0,p[0,:]> (L/2)] - L

            tmp_p[1, p[1,:] > L/2] = tmp_p[1, p[1,:] > (L/2)] - L

            tmp_p[0, p[0,:] < -L/2]  = tmp_p[0, p[0,:] < (-L/2)] + L

            tmp_p[1, p[1,:] < -L/2]  = tmp_p[1, p[1,:] < (-L/2)] + L



            p = tmp_p
            p_plot.append(p)

            # Can Also be written as:

            # p[p > limit] -= limit * 2

            # p[p < -limit] += limit * 2



            line1, = ax.plot(p[0, 0], p[1, 0])
            #print(p[0, 0], p[1, 0])



            #update plot

            ax.clear()

            ax.quiver(p[0,:], p[1,:], v[0,:], v[1,:]) # For drawing velocity arrows, at position 

            plt.xlim(-limit, limit)

            plt.ylim(-limit, limit)

            line1.set_data(p[0,:], p[1,:])


            print(f"Frame: {i}")
   

            fig.canvas.draw()
            fig.canvas.start_event_loop(interval)
    

    #def update(p, v, r):

        


flock_py = flock()

flock_py.flocking_python()

