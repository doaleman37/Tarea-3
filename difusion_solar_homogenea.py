import numpy as np
import matplotlib.pyplot as plt
import sys

m=sys.argv[1]
n=int(m)

c=np.random.random(n)
r=(c**(1.0/3.0))*100
t=np.random.random(n)
th=2.0*((np.pi)*t)
k=np.random.random(n)
kh=np.arccos((2.0*k)-1.0)
x=np.sin(kh)*(np.cos(th)*r)
y=np.sin(kh)*(np.sin(th)*r)
z=r*np.cos(kh)

Pasos=np.zeros(n)
Distancia=np.sqrt(x**2 + y**2 + z**2)

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
plt.show()
