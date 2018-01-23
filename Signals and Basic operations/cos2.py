import numpy as np 
import matplotlib.pyplot as plot

n = np.arange(-20,20,1);  # Range of n 
x_n = np.cos((n*np.pi)/8)*np.exp(-0.1*n)
plot.stem(n,x_n)
plot.show()			