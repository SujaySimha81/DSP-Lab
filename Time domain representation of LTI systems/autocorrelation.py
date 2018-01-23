import numpy as np 
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

s=np.random.uniform(-1,1,499)
n=np.arange(0,499,1)
x1=np.sin(0.1*np.pi*n)
x=np.sin(0.1*np.pi*n)+s
plt.stem(n,x1)
plt.show()

plt.stem(n,x)
plt.show()
k=np.arange(-499,498)
ac=sig.correlate(x,x)
plt.plot(k,ac)
plt.show()

i=np.ones(500)

k1=np.arange(-499,499)
cc=sig.correlate(s,i)
plt.plot(k1,cc)
plt.show()

