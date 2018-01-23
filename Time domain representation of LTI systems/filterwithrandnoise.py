import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig

w=np.random.rand(60)
n=np.arange(0,60,1)
x1=0.1*n+np.sin(0.1*n*np.pi)

a1=[1]
b1=[0.25,0.25,0.25,0.25]
resp1=sig.lfilter(b1,a1,x1)
plt.stem(n,resp1)
plt.show()

a2=[1]
b2=[0.1,0.2,0.3,0.4]
resp2=sig.lfilter(b2,a2,x1)
plt.stem(n,resp2)
plt.show()

a3=[-0.75,1]
b3=[0.25]
resp3=sig.lfilter(b3,a3,x1)
plt.stem(n,resp3)
plt.show()

# With Noise
w=np.random.uniform(-5,5,60)
n=np.arange(0,60,1)
x1=0.1*n+np.sin(0.1*n*np.pi)+w

a1=[1]
b1=[0.25,0.25,0.25,0.25]
resp1=sig.lfilter(b1,a1,x1)
plt.stem(n,resp1)
plt.show()

a2=[1]
b2=[0.1,0.2,0.3,0.4]
resp2=sig.lfilter(b2,a2,x1)
plt.stem(n,resp2)
plt.show()

a3=[-0.75,1]
b3=[0.25]
resp3=sig.lfilter(b3,a3,x1)
plt.stem(n,resp3)
plt.show()
