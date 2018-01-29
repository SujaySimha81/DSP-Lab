import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

b=np.ones(5)
a=[1]
c=np.arange(-2*np.pi, 2*np.pi, 4*np.pi/4096)
print(len(c))
w1,h1=sig.freqz(b,a,c)
print((w1))
h1db=20*np.log10(abs(h1))
plt.plot(w1/(2*np.pi),h1db)
plt.show()
angles = np.angle(h1)
plt.plot(w1/(2*np.pi), angles, 'g')
plt.show()

#2
x1=np.zeros(7)
x1=np.append(x1,b)
w2,h2=sig.freqz(x1,a,c)
h2db=20*np.log10(abs(h2))
plt.plot(w2/(2*np.pi),h2db)
plt.show()
angles1 = np.angle(h2)
plt.plot(w2/(2*np.pi), angles1, 'g')
plt.show()

#3
x2=[0,0,0,0,1]
w3,h3=sig.freqz(b,x2,c)
h3db=20*np.log10(abs(h3))
plt.plot(w3/(2*np.pi),h3db)
plt.show()
angles2 = np.angle(h3)
plt.plot(w3/(2*np.pi), angles2, 'g')
plt.show()

#4 Same as part 3
#5
x3=[1,-1,1,-1,1]
w4,h4=sig.freqz(x3,a,c)
h4db=20*np.log10(abs(h4))
plt.plot(w4/(2*np.pi),h4db)
plt.show()
angles4 = np.angle(h4)
plt.plot(w4/(2*np.pi), angles4, 'g')
plt.show()

