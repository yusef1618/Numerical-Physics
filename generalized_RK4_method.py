#In this code we solve an ordinary differential equation using the 4th order Runge Kutta method

import numpy as np
import matplotlib.pyplot as plt

#We define the rk4 method function
#For more information, see: 
#Rubin H. Landau, Manuel J. Paez, Cristian C. Bordeianu: Computational Physics Problem Solving with Python-Wiley-VCH (2015) p.178, 185
def rk4(y,t,h,f):
	k1 = h*f(t,y)
	k2 = h*f(t+h/2,y+k1/2)
	k3 = h*f(t+h/2,y+k2/2)
	k4 = h*f(t+h,y+k3)
	y=y+(k1+2*(k2+k3)+k4)/6
	return y

#Using the standard form for ODE's dy/dt = t**2
#RK4 will solve this equation
def f1(t, y):
    return t**2

#This ODE has analytic solution, which is g(t)
#Not every ODE has analytic solution (that's why we solve some of them numerically)
#But this time it's just to see graphically how much the RK4 algorithm deviates from the actual solution
def g(t):
    return 1/3*t**3

#tau is the time the simulation runs
tau = 15
#N is the number of intervals we divide the tau on
N = 1000
#h1 is the step, this relation is MANDATORY for the RK4 algorithm to work properly
#(if you want try it by yourself, use different values for h1, e.g: 0.1)
h1 = tau/N

#This is the time divided by an equally number of subintervals
t = np.linspace(0, tau, N)
#We create a 1 column matrix with N zeros to later save the values of the 
#solved ODE there
A = np.zeros([N,1])

#This loop fills the A matrix with the numerical solution
for j in range(N-1):
    A[j+1] = rk4(A[j], t[j], h1, f1)

#We plot the analytic solution along with the numerical one
plt.plot(t, g(t), '-r', label = "Analytic solution")
plt.plot(t, A, '--b', markersize=1, label = "4th order RK method")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Analytic vs RK4 solutions = f(x)")
plt.legend()
plt.grid()
plt.show()
