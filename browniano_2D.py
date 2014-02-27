import numpy as np
import matplotlib.pyplot as plt
import sys

m=sys.argv[1]
n=int(m)


angulo =np.random.random(n)
pasox=np.cos(2.0*np.pi*angulo)
pasoy=np.sin(2.0*np.pi*angulo)
Distancia_x=np.zeros(n)
Distancia_y=np.zeros(n)
Distancia_al_origen=np.zeros(n)

for i in range(1,n):
    Distancia_x[i]=Distancia_x[i-1]+pasox[i-1]
    Distancia_y[i]=Distancia_y[i-1]+pasoy[i-1]


for i in range(n):
    Distancia_al_origen[i]=np.sqrt((Distancia_x[i]**2.0)+(Distancia_y[i]**2.0))
    
Numero_de_pasos=np.zeros(n)

for i in range(n):
    Numero_de_pasos[i]=i+1



plt.plot(Numero_de_pasos,Distancia_al_origen)
plt.savefig("Browniano_2D_n.pdf")
plt.show()
