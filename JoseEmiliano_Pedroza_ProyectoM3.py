import numpy as np
import matplotlib.pyplot as plt
from random import randint

#Aquí definí el numero de canicas y niveles que tendrá el simulador.
canicas = 3000
niveles = 12

np.random.randint(2, size=niveles)#Usé esta funcion para crear un arreglo de 2 dimensiones (simular derecha o izquierda)
#tomando como tamaño el numero de niveles. 
recorrido = np.random.randint(2, size=niveles)
np.sum(recorrido)

resultado = []
#Aqui se usa una lista para contener el final del recorrido de las canicas
for i in range(canicas):
    recorrido = np.random.randint(2, size=niveles)
    posicion_final = np.sum(recorrido)
    resultado.append(posicion_final)
#En esta seccion se grafican los resultados en un histograma el cual adquirirá la forma de la campana gaussiana
plt.hist(resultado)
plt.xlabel("Distribucion de canicas")
plt.ylabel("Cantidad de canicas")
plt.title("Simulador: Maquina de Galton")
plt.show()