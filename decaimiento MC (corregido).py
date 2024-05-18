import numpy as np
import matplotlib.pyplot as plt

#Definimos los parametros fisicos del problema

d = 20 #m
m = 139.6 #MeV
K = 200 #MeV
c = 3e8

tau = 2.6e-8 #s
print(f"Tiempo de vida: {tau}")

gamma = (K/m) + 1
print(f"gamma: {gamma}")

v = c*(np.sqrt(1 - 1/gamma**2))
print(f"Velocidad: {v}")
print(f"Fraccion de la velocidad de la luz: {v/c} c")

t = d/v
#t= 20
print(f"Tiempo en el que atrviesa la particula los 20m: {t}")

#dt son las veces que una particula puede decaer durante los 20m
dt = t / tau
#redondeamos dt
#dt = round(dt)
#print(f"Cantidad de veces que le preguntamos a la particula si decayó: {dt}")

tiempo = np.linspace(0, t, 10)

lambda1 = 0.1
print(f"Valor de lambda: {lambda1}")



def f():
  prueba = 0
  for i in tiempo:               #range(dt):
    dec = np.random.rand()
    if dec < lambda1:
      prueba = 0
      break
    else:
      prueba = 1
    
  return prueba

N_in = 10**6
tot = 0
for j in range(N_in):
    tot = tot + f()

print(f'Cantidad de partículas que sobrevivieron: {tot}')
porc = (tot*100)/N_in
print(f'Porcentaje de partículas que sobrevivieron: {porc}%')
