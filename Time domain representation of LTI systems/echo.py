import numpy as np 
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

rate, data = wav.read('atmospace_jungle.wav',mmap=False)
N1=1
N2=2
n=np.arange(0,len(data))
a=[1]
b=[0.6,0.8,1]
resp2=sig.lfilter(b,a,data)
wav.write('voice.wav',rate,resp2)
