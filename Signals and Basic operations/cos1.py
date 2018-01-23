import numpy as np 
import matplotlib.pyplot as plot

n = np.arange(-20,20,1)  # Range of n 
x_n = 3*np.cos(0.25*n*np.pi + np.pi/3.0)
plot.stem(n,x_n)
plot.show()