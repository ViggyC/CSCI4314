import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pylab


class random_walks_python():
    def random_walks(self):
        N = 500  # no of steps per trajectory
        realizations = 50  # number of trajectories
        v = 1.0  # velocity (step size)
        current_step = 0
        #use these three angles for each w, three plots for each of the three w's
        theta_s_array = [round(math.pi / 24, 4), round(math.pi / 12, 4), round(math.pi / 3,
                                                                               4)]  # the width of the random walk turning angle distribution (the lower it is, the more straight the trajectory will be)
       #plot for each of these
        w_array = [0.0, 0.5,
                   1.0]  # w is the weighting given to the directional bias (and hence (1-w) is the weighting given to correlated motion)
        ratio_theta_s_brw_crw = 1
        plot_walks = 1
        count = 0

        efficiency_array = np.zeros([len(theta_s_array), len(w_array)])
        new_efficiency_array = [[],[],[]]
        #print(efficiency_array)
        w_1 = [[], [], []]
        w_half = [[], [], []]
        w_0 = [[], [], []]
        #each w array will hold the mean navigational efficiency for different angle
        arrays = [w_0, w_half, w_1]
        total_distance_moved = 0
        # for w_i in range(len(w_array)):
        #     w = w_array[w_i] #pure biased walk, pure correlated walk, both
        #     for theta_s_i in range(len(theta_s_array)):
        #         #run time step sim here?
        #         theta_s_crw = np.multiply(ratio_theta_s_brw_crw, theta_s_array[theta_s_i])
        #         #print(theta_s_crw)
        #         theta_s_brw = theta_s_array[theta_s_i]
        #         x, y, arr = self.BCRW(N, realizations, v, theta_s_crw, theta_s_brw, w)
        #         print(arr)
        #         if plot_walks == 1:
        #             count += 1
        #             plt.figure(count)
        #             plt.plot(x.T, y.T)
        #             plt.axis('equal')
        #         #pi = pi/24,, pi/12, pi/3 for each w = 0,0.5,1
                
                
        #         #this is the final navigational efficientcy
        #         efficiency_array[theta_s_i, w_i] = np.divide(np.mean(x[:, -1] - x[:, 0]), (v * N))

        #         #efficiency_array_plot[theta_s_i, w_i] = np.divide(np.mean(x[:, -1] - x[:, 0]), (v * N))
        #         #print(efficiency_array)
        #         #print(f"Navigational efficiency at {theta_s_array[theta_s_i]} for w={w} is: {efficiency_array[theta_s_i, w_i]}")
        #         arrays[w_i][theta_s_i] = arr

        #paet 2        
        for w_i in range(len(w_array)):
            w = w_array[w_i] #pure biased walk, pure correlated walk, both
            #run time step sim here?
            new_ratio_theta_s_brw_crw = round(math.pi / 3, 4)/ round(math.pi / 3, 4)
            theta_s_crw = np.multiply(new_ratio_theta_s_brw_crw, round(math.pi / 3, 4))
            #print(theta_s_crw)
            theta_s_brw = round(math.pi / 3, 4)
            x, y, arr = self.BCRW(N, realizations, v, theta_s_crw, theta_s_brw, w)
            #print(arr)
            if plot_walks == 1:
                count += 1
                plt.figure(count)
                plt.plot(x.T, y.T)
                plt.axis('equal')
            #pi = pi/24,, pi/12, pi/3 for each w = 0,0.5,1
            
            
            #this is the final navigational efficientcy
            new_efficiency_array[w_i] = np.divide(np.mean(x[:, -1] - x[:, 0]), (v * N))

            #efficiency_array_plot[theta_s_i, w_i] = np.divide(np.mean(x[:, -1] - x[:, 0]), (v * N))
            #print(efficiency_array)
            #print(f"Navigational efficiency at {theta_s_array[theta_s_i]} for w={w} is: {efficiency_array[theta_s_i, w_i]}")
        
            
            # plt.show()
        #print(efficiency_array)
        plt.figure()
        legend_array = []
        w_array_i = np.repeat(w_array, len(efficiency_array))
        print(f"Efficiency: {new_efficiency_array}")
        #w = 0
        plt.title('w = 0')
        plt.xlabel("Timestep")
        plt.ylabel("Navigational Efficiency")
        plt.plot(arrays[0][0][1::], label = "pi/24")
        plt.plot(arrays[0][1][1::], label = "pi/12")
        plt.plot(arrays[0][2][1::], label = "pi/3")
        plt.legend()

        plt.figure() #w = 0.5
        plt.title('w = 0.5')
        plt.xlabel("Timestep")
        plt.ylabel("Navigational Efficiency")
        plt.plot(arrays[1][0][1::], label = "pi/24")
        plt.plot(arrays[1][1][1::], label = "pi/12")
        plt.plot(arrays[1][2][1::], label = "pi/3")
        plt.legend()

        plt.figure() #w = 1
        plt.title('w = 1')
        plt.xlabel("Timestep")
        plt.ylabel("Navigational Efficiency")
        plt.plot(arrays[2][0][1::], label = "pi/24")
        plt.plot(arrays[2][1][1::], label = "pi/12")
        plt.plot(arrays[2][2][1::], label = "pi/3")
        plt.legend()


   

        #what does this loop do?
        for theta_s_i in range(0, len(theta_s_array)):
            legend_array.append(
                ["$\theta^{*CRW}=$", (ratio_theta_s_brw_crw * theta_s_array[theta_s_i]), "$\theta^{*BRW}=$",
                 (theta_s_array[theta_s_i])])

        
        plt.figure()
        plt.xlabel('w')
        plt.ylabel('navigational efficiency')
        plt.plot(w_array, efficiency_array[0], 'bo', label=legend_array[0])
        plt.plot(w_array, efficiency_array[1], 'go', label=legend_array[1])
        plt.plot(w_array, efficiency_array[2], 'ro', label=legend_array[2])
       
        
        plt.legend(loc='best', prop={'size': 5.2})
        plt.show()
 

        

  
        



    # The function generates 2D-biased correlated random walks
    def BCRW(self, N, realizations, v, theta_s_crw, theta_s_brw, w):
        X = np.zeros([realizations, N])
        Y = np.zeros([realizations, N])
        theta = np.zeros([realizations, N])
        X[:, 0] = 0
        Y[:, 0] = 0
        theta[:, 0] = 0
        array = np.zeros(N) #size = 500

        for realization_i in range(realizations):
            count = 0
            for step_i in range(1, N):
                #print(step_i)
                count += 1
                theta_crw = theta[realization_i][step_i - 1] + (theta_s_crw * 2.0 * (np.random.rand(1, 1) - 0.5))
                theta_brw = (theta_s_brw * 2.0 * (np.random.rand(1, 1) - 0.5))

                X[realization_i, step_i] = X[realization_i][step_i - 1] + (v * (w * math.cos(theta_brw))) + (
                            (1 - w) * math.cos(theta_crw))
                Y[realization_i, step_i] = Y[realization_i][step_i - 1] + (v * (w * math.sin(theta_brw))) + (
                            (1 - w) * math.sin(theta_crw))

                current_x_disp = X[realization_i][step_i] - X[realization_i][step_i - 1]
                current_y_disp = Y[realization_i][step_i] - Y[realization_i][step_i - 1]
                current_direction = math.atan2(current_y_disp, current_x_disp)

                theta[realization_i, step_i] = current_direction
        #need to somehow calc the nav eff at each time step
                #array.append(np.divide(np.mean(X[:, step_i] - X[:, 0]), (v * step_i)))
                array[step_i] = np.divide(np.mean(X[:, step_i] - X[:, 0]), (v * step_i))
                #print(array[step_i])
             
        #print(array)
        return X, Y, array


rdm_plt = random_walks_python()
rdm_plt.random_walks()
