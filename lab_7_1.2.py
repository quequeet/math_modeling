import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 3

x = R * t * np.cos(t) ** 3 
y = R * t * np.sin(t) ** 3  

plt.plot(x, y, ls='-', lw=3)

plt.axis('equal')

plt.savefig('pic_7.png')