#import numpy as np
import matplotlib.pyplot as plt

#defining the magnetic field

Bx=0    #T
By=0    #T
Bz=1    #T

#defining the initial velocity

vxo=1   #m/s
vyo=1   #m/s
vzo=1   #m/s

vx=[vxo]
vy=[vyo]
vz=[vzo]

#defining the particle characteristics

q=1     #C
m=1     #kg

#---------------------------------------------------------------------
#------------Euler's method----velocity-------------------------------
#---------------------------------------------------------------------

i=0
j=100000
h=(1/j)*(10**2)  #step
a=q/m

t=[0]
while i != j:
    vx.append(a*(vy[i]*Bz-vz[i]*By)*h+vx[i])
    vy.append(a*(vz[i]*Bx-vx[i]*Bz)*h+vy[i])
    vz.append(a*(vx[i]*By-vy[i]*Bx)*h+vz[i])
    t.append(t[i]+h)
    i+=1
#-------------------------------------------------------------------
#-----------defining the space characteristics----------------------
#-------------------------------------------------------------------

xo=0
yo=0
zo=0

x=[xo]
y=[yo]
z=[zo]

#---------------------------------------------------------------------
#------------Euler's method----space----------------------------------
#---------------------------------------------------------------------
i=0

while i!= len(vx):
    x.append(vx[i]*h+x[i])
    y.append(vy[i]*h+y[i])
    z.append(vz[i]*h+z[i])
    i+=1


ax=plt.axes(projection='3d')

plt.plot(x,y,z)
plt.show()

