import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='y', label='Ball', ms=85)

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = - 0.007 * time ** 2 + 0.5* time - 5
    alpha = np.arange(0, 2*np.pi, 100)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y
 
edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(circle_move(R= -8, vx0=0.2, vy0=0.01, time=i))
  
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30)
                              
ani.save('sunrise.gif')