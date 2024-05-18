#This program uses Monte Carlo method to determine how many radioactive particles
#decay in a given the half-life time of the particle, it's kinetic energy and the distance traveled

import numpy as np
import matplotlib.pyplot as plt

#We define the phyisical parameters of the problem

#Distance in meters
d = 20 #m
#Mass 
m = 139.6 #MeV/c^2
#Kinetic energy
K = 200 #MeV
#Speed of light
c = 3e8 #m/s

#Half-life time of the particle
tau = 2.6e-8 #s
print(f"Half life time: {tau}")

#Relativistic factor
gamma = (K/m) + 1
print(f"gamma: {gamma}")

#We calculate the velocity of the particle in the lab system
#and using the distance, calculate the time it takes to travel the distance
v = c*(np.sqrt(1 - 1/gamma**2))
print(f"Velocity of the particle: {v}")
print(f"Fraction of the speed of light: {v/c} c")

t = d/v
print(f"Time it takes the particle to travel 20m: {t}")

#Divide the time between the half-life time to verify how much times it can decay in the trajectory
dt = t / tau
#Round dt
#dt = round(dt)
#print(f"How many times we ask the particle if it decayed: {dt}")

time = np.linspace(0, t, 10)

lambda1 = 0.1
print(f"lambda factor: {lambda1}")

#This function decides whether the particle decays or not in the time interval
def f():
  test = 0
  for i in time:               #range(dt):
    dec = np.random.rand()
    if dec < lambda1:
      test = 0
      break
    else:
      test = 1
    
  return prueba

#We give an initial number of particles to be examined
N_in = 10**6
tot = 0
#And use the function to make a counter of the decayed particles
for j in range(N_in):
    tot = tot + f()


print(f'Particles thar survived: {tot}')
porc = (tot*100)/N_in
print(f'Percentage of particles that survived: {porc}%')
