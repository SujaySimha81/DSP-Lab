import numpy as np 
import matplotlib.pyplot as plt

t = np.arange(0,3,1/20)
s1 =np.cos(10*np.pi*t)
plt.stem(t,s1)
plt.show()

t1 = np.arange(0,3,2/15)
s2 =np.cos(10*np.pi*t1)
plt.stem(t1,s2)
plt.show()

t2 = np.arange(0,3,1/5)
s3 =np.cos(10*np.pi*t2)
plt.stem(t2,s3)
plt.show()

t3 = np.arange(0,3,2/5)
s4 =np.cos(10*np.pi*t3)
plt.stem(t3,s4)
plt.show()