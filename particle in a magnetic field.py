import numpy as np
#from numpy import linalg as la
import matplotlib.pyplot as plt
import math

vxo=1
vyo=0
vzo=0

vo=np.array([vxo,vyo,vzo])

Bx=0
By=0
Bz=10

B= np.array([Bx,By,Bz])

q=-1     #particle charge
m=1     #particle mass

C=np.cross(vo,B)

f=q*C   #magnetic force acting on the particle
a=f/m   #acc.


vx=[vxo]
vy=[vyo]
fvx=[(q*Bz/m)*vx[0]]
fvy=[(q*Bz/m)*vy[0]]


i=0
t=0.0001
tf=10
j=tf/t

ts=[0]
v=[]

while i!=j:

    vy.append(-(fvx[i])*t+vy[i])
    vx.append((fvy[i])*t+vx[i])
    fvx.append((q*Bz/m)*vx[i+1])
    fvy.append((q*Bz/m)*vy[i+1])
    v.append(np.sqrt(vx[i]**2+vy[i]**2))
    ts.append(ts[i]+t)
    i+=1
    

print("R=",round(np.sqrt((m*v[-1]/(q*Bz))**2),4),"m")
print("v=",np.sqrt(vx[-1]**2+vy[-1]**2), "m/s")


xo=0
yo=0
zo=0
x=[xo]
y=[yo]
X=np.array([[],[]])
Y=np.array([[],[]])

i=0
while i != len(ts):
    x.append(x[i]+vx[i]*t)
    y.append(y[i]+vy[i]*t)
    i+=1




x.remove(x[-1])
y.remove(y[-1])

i=0
z=[zo]
while i != len(x):
    z.append(z[i]+vzo*ts[i])
    i+=1
    
z.remove(z[-1])

ax=plt.axes(projection='3d')
ax.scatter(x,y,z)

plt.show()
