#The following program uses the Runge-Kutta algorithm to solve the movement 
#equations for a particle in a parabolic shot, thus, obtaining the graph of the 
#movement of the particle


import numpy as np
import matplotlib.pyplot as plt

# Parameters of the simulation

N = 100000                 # Number of steps 
tau = 1500                 # Time of the simulation
h = tau / float(N - 1)     # Step size 
g = 9.81                   # Acceleration due to gravity 
m = 1                      # Mass (irrelevant)
v0 = 600                   # Initial velocity
x0 = 0                     # Initial position in x
y0 = 0                     # Initial position in y
theta_0 = np.deg2rad(60)   # Angle of the shot in radians


# We calculate both of the components of the initial velocity
v0_x = v0 * np.cos(theta_0) 
v0_y = v0 * np.sin(theta_0)  


# Values of the friction coefficient
k_values = [0, 0.08, 0.04, 0.02, 0.01, 0.005]

# Funcion para calcular las posiciones en funcion del tiempo para un valor dado de k
#We create a function to calculate the position with respect of time for a given value of k
def simular_lanzamiento(k):

    #This is the ODE written in standar form
    #The notation f0,...,f3 might be confusing, but it is about the following derivatives:
    #f0 = f^(1)
    #f1 = f^(2)
    #f2 = g^(1)
    #f3 = g^(2)
    
    #Where f^(1) = dx/dt y g^(1) = dy/dt
    
    def f(t, y):        
        #Velocity moduli
        v = np.sqrt(y[1]**2 + y[3]**2)
        f0 = y[1]
                
        #Here we use the fact that F_roz = -mk v_x^2* v_x/v
        f1 = -k *(f0**3)/v
        #y
        f2 = y[3]
        #dy/dt
        f3 = -g - k *(f2**3)/v
        return np.array([f0, f1, f2, f3])
 
    # Initialization of the variables and arrays
    tiempo = np.linspace(0, tau, N)
    
    A = np.zeros([N, 4])
    
    A[0, 0] = x0
    A[0, 1] = v0_x
    
    A[0, 2] = y0
    A[0, 3] = v0_y
        

    # Simulation of the shot
    for j in range(N-1):
        A[j+1] = rk4(A[j], tiempo[j], h, f)
        
        # Tolerance used to detect collision with the ground
        if A[j+1, 2] < 0:  
            break

    # Return the positions (x and y) and saves it
    return A[:, 0], A[:, 2]  

#Runge Kutta 4 
def rk4(y, t, h, f):
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    y=y+(k1+2*(k2+k3)+k4)/6
    return y


# Do the simulation and plot the results
plt.figure(figsize=(10, 6))
for k in k_values:
    position_x, position_y = simular_lanzamiento(k)
    plt.plot(position_x, position_y,  '.', markersize=1, label=f'k={k}')

plt.xlabel('Position in x (m)')
plt.ylabel('Position in y (m)')
plt.title('Trayectories for different k values')
plt.legend()
plt.grid(True)
plt.show()
