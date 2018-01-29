##code
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
x=np.array([0,1,2,3])
a=[1]
n=np.arange(0,10)
c=np.arange(-2*np.pi, 2*np.pi, 4*np.pi/4096)
w1,h1=sig.freqz(x,a,c)

y=np.power(0.9,n)
w2,h2=sig.freqz(y,a,c)

z=np.multiply(h1,h2)
h1db=20*np.log10(abs(h1))
h2db=20*np.log10(abs(h2))
h3db=20*np.log10(abs(z))

plt.plot(w1/(2*np.pi),h1db)
plt.show()
plt.plot(w1/(2*np.pi),h2db)
plt.show()
plt.plot(w1/(2*np.pi),h3db)
plt.show()

angles = np.angle(h1)
plt.plot(w1/(2*np.pi), angles, 'g')
plt.show()
angles1 = np.angle(h2)
plt.plot(w1/(2*np.pi), angles1, 'g')
plt.show()
angles2 = np.angle(z)
plt.plot(w1/(2*np.pi), angles2, 'g')
plt.show()

conv=np.convolve(np.append(
    
x,np.zeros(6)),y)
w4,h4=sig.freqz(conv,a,c)
h4db=20*np.log10(abs(h4))
plt.plot(w4/(2*np.pi),h4db)
plt.show()