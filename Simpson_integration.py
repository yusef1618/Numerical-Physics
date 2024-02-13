#One way of integrating functions is via the Simpson rule for integration, here we present the code to integrate a generic function 
#over the interval (0, 5)
#For more information see: 
#Rubin H. Landau, Manuel J Paez, Cristian C. Bordeianu: Computational Physics Problem Solving with Python-Wiley-VCH (2015) p.94

import numpy as np

#We define a generic function, in this case, x
def f(x):
    return x

#Lower limit of the interal
a = 0
#Upper limit of the interal
b = 6

#Number of divisions for the interval (change deppending of your needs)
n = 100

#Step value 
h = (b-a)/n

#Initialize the odd and even sums
#sumo = odd sum, sume = even sum
sumo = 0
sume = 0

#Sum of the function evaluated in the odd intervals
for i in range (1,n,2):
    xi = a + i*h
    sumo = sumo + f(xi)

#Sum of the function evaluated in the even intervals
for j in range(2,n,2):
    xj = a + j*h
    sume = sume + f(xj)
    

#Value of the integral 
I = (b-a) * (f(a) + 4* sumo + 2*sume + f(b))/(3*n)

print(f"Numerical value of the integral :{I}")
