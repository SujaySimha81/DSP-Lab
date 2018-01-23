import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig
a=[0.2,0.2,0.5]
b=[0.25,-0.5,1]
t1,c1=sig.impulse((a,b))
plt.stem(t1,c1)
plt.show()

a1=np.array([0,1,1])
b1=np.array([0,-0.77,1])
t2,c2=sig.impulse((a1,b1))
plt.stem(t2,c2)
plt.show()

a2=np.array([0,1,0.77])
b2=np.array([0,-0.77,1])
t3,c3=sig.impulse((a2,b2))
plt.stem(t3,c3)
plt.show()

T1,step1=sig.step((a,b))
plt.stem(T1,step1)
plt.show()

T2,step2=sig.step((a1,b1))
plt.stem(T2,step2)
plt.show()

T3,step3=sig.step((a2,b2))
plt.stem(T3,step3)
plt.show()