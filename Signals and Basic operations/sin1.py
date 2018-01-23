import numpy as np 
import matplotlib.pyplot as plot

n = np.arange(-20,20,1);  # Range of n 
x_n = (np.sin((n*np.pi)/6))/((n*np.pi)/6) 
plot.stem(n,x_n)
plot.show()