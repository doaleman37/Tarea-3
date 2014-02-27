import numpy as np
import matplotlib.pyplot as plt
import sys

m=sys.argv[1]
n=int(m)

x=np.zeros(n)
y=np.zeros(n)
z=np.zeros(n)
Pasos=np.zeros(n)
Distancia=np.zeros(n)

for i in range(n):
  while Distancia[i]<100:
    theta=2.0*(np.pi*np.random.random())
    phi=2.0*(np.pi*np.random.random())
    x[i]=x[i]+((np.sin(theta))*(np.cos(phi)))
    y[i]=y[i]+(np.sin(theta))*(np.sin(phi))
    z[i]=z[i]+(np.cos(theta))
    Pasos[i]=Pasos[i]+1
    Distancia[i]=np.sqrt(x[i]**2 + y[i]**2 + z[i]**2)

plt.hist(Pasos, bins=50)
plt.savefig("Histo_difusion_solar_central_n.pdf")
plt.show()
