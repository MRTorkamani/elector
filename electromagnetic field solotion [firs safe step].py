import numpy as n
import matplotlib.pyplot as plt
import matplotlib.animation as animation

m=1e-31
q=1e-19
B=1e-8
k=9e9
h=1e-8


vx = [0]
vy = [0]
x  = [0]
y  = [-2.7e-2]
ax = [0]
ay = [0]
timestep=900000
def teta(vy,vx):
	if vx<1e-150:
		return n.pi/2
	else:
		return n.arctan(vy/vx)
for i in range(timestep):
	ax.append((q*B/m)*(vx[-1]**2 + vy[-1]**2)**(1/2)*round(n.sin(teta(vy[-1],vx[-1])),15))
	ay.append(k*(q**2/(m*(2*y[-1])**2))-(q*B/m)*(vx[-1]**2+vy[-1]**2)**(1/2)*round(n.cos(teta(vy[-1],vx[-1])),15))
	vx.append(h*ax[-1]+vx[-1])
	vy.append(h*ay[-1]+vy[-1])
	x.append(h*vx[-1]+x[-1])
	y.append(h*vy[-1]+y[-1])

t=[0]
for i in range(timestep):
	t.append(t[i]+h)	
#print(x)
#print(y)

#print(len(x))
#print(len(t))
plt.plot(x,y)

newy=[-1*i for i in y ]
plt.plot(x,newy)
#plt.show()

plt.show()

#print(ay[1],ay[2],ay[3],ay[4])
#print(ax[1],ax[2],ax[3],ax[4])
