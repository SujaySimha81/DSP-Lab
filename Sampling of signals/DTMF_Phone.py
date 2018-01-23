import numpy as np 
import scipy.io.wavfile as wav
a=np.zeros(100)
f1=np.array([941,697,697,697,770,770,770,852,852,852])
f2=np.array([1336,1209,1336,1477,1209,1336,1477,1209,1336,1477])
t=np.arange(0,0.4,1/8192)
s1=[]
s2=[]
n=[0,8,2,4,2,4,7,4,0,4,0]
for i in n:
    s1=np.sin(np.pi*t*2*f1[i])+np.sin(np.pi*t*2*f2[i])
    s2=np.append(s2,s1)
    s2=np.append(s2,a)
wav.write('phone.wav',8192,s2)