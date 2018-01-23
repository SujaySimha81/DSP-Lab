import numpy as np 
import matplotlib.pyplot as plot

n = np.arange(-20,20,1);  # Range of n 
x_n = np.power(-0.75,n)
for i in range(0,20):
    x_n[i]=0
plot.stem(n,x_n)
plot.show()