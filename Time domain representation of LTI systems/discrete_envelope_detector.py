import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig
ts=0.01
n=np.arange(0,100)
p=np.ones(20)
p=np.append(p,np.zeros(20))
p=np.append(p,np.ones(20))
p=np.append(p,np.zeros(40))

x=np.cos(20*np.pi*ts*n)*p
plt.stem(n,x)
plt.show()
y=np.absolute(x)
plt.stem(n,y)
plt.show()
print(len(y))
o=np.ones(15)
o=np.append(o,np.zeros(75))*(1/15)
cv=np.convolve(y,o)

r=np.arange(-95,94)
plt.stem(r,cv)
plt.show()