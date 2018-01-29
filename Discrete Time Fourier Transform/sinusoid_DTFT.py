import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
a=[1]
n=np.arange(0,22)
cos=2*np.cos(((np.pi/4)*n)+np.pi/6)
c=np.arange(-np.pi, np.pi, 2*np.pi/4096)
w1,h1=sig.freqz(cos,a,c)
print((w1))
h1db=20*np.log10(abs(h1))
plt.plot(w1/(2*np.pi),h1db)
plt.show()
angles = np.angle(h1)
plt.plot(w1/(2*np.pi), angles, 'g')
plt.show()

#2
n1=np.arange(0,202)
cos2=2*np.cos(((np.pi/4)*n1)+np.pi/6)
w1,h1=sig.freqz(cos2,a,c)
print((w1))
h1db=20*np.log10(abs(h1))
plt.plot(w1/(2*np.pi),h1db)
plt.show()
angles = np.angle(h1)
plt.plot(w1/(2*np.pi), angles, 'g')
plt.show()