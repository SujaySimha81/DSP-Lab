import numpy as np 
import matplotlib.pyplot as plot
n = np.arange(-20,20,1);  # Range of n 
x_n=2*np.cos(0)+4*np.cos((np.pi*n)/20.0-np.pi/5)+3*np.cos((3*np.pi*n)/40.0-np.pi/2.0)+4*np.cos((3*np.pi*n)/20.0-np.pi/3.0)
plot.stem(n,x_n)
plot.show()