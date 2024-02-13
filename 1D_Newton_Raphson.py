#One of the most useful tools in physics is the Newton-Raphson method for root finding.
#Here, I present a code that finds the root fot a generic function using the 1-D Newton-Raphson method.
#This can be modified to find, for example:
#The numerical values of the energies of the finite square well
#A constant for the least square method to fit a graph onto a set of data
#etc...

import numpy as np
import matplotlib.pyplot as plt

#Newton Raphson

def NewtonRaphson(f, df, p_0, tol = 10**-4, n =50):
    """
    Newton Raphson
    ----------
    f : Function to which root will be found
    df : Numerical derivative of the function (the use of forward or extended difference is recommended )  
    p_0 : Seed for the method (The convergence of the method relies in the initial value, be careful with functions with max and min valuees)
    tol : Tolerance, used as a stop criteria 
    n : Max number of iterations, another stop criteria

    Return: Exact or approximated root for the function, None in case of divergence or derivative at one point = 0
    """
    #Prints the first iteration and the seed used 
    print('ite{:<2}: p_{:<2}={:.7f}'.format(0,0,p_0))
    
    #Start the absolute error variable
    e_abs = 0
    #Start the variable i that will be used for iteration
    i = 1

    #While loop that:
    #Returns None in case the number of iterations is exceeded
    #Returns the root if the absolute value of the error is less than the tolerance
    #Returns None in case that derivative = 0 (prohibits the division by 0)
    
    while i <= n:
        
        #Forbid the division by 0
        if df(p_0) == 0: 
            print('Solution not found')
            return None
        
        #1D Newton-Raphson
        p_1 = p_0 - (f(p_0))/(df(p_0))  
        e_abs = abs(p_1 - p_0)
        print('ite{:<2}: p_{:<2}={:.7f}, e_abs={:.7f}'.format(i,i,p_1, e_abs))
        
        #Stop criteria 
        if e_abs < tol:
            print('Solution found x = {:.7f}, iteraciones:{}'.format(p_1, i))
            return p_1
        
        p_0 = p_1
        i += 1
    #If the number of iterations is exceeded, that stops the loop
    print('Solution not found, exceeded iterations: {}'.format(i-1))
    return None


#We define a generic function (change depending of you needs)
def f(x):
    return x**3 + 4*(x**2) - 10

#Forward difference 
#Give a numerical value to the steps of the derivative
h = 0.01

#We write the derivative
def fd(x):
    return ( f( x+ h) - f(x) )/h

#We calculate the root using the Newton Raphson method, and give the value of the seed
root = NewtonRaphson(f, fd, 10)

#Divide the -10,10 interval in 200 for plotting the function
x = np.linspace(-10,10, 200)
plt.grid(True)
#Plot the root of the function
plt.plot(root, 0, '.', label = "Root")
#Plot the function in the interval
plt.plot(x, f(x), label = "Funcion generica")
plt.ylim(-20,20)
plt.legend()
