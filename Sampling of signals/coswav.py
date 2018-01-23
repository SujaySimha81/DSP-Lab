import numpy as np 
import scipy.io.wavfile as wav

rate = 8000;
t = np.arange(0,3,1/8000)
s1 =np.cos(1000*np.pi*t)
wav.write('cos1000.wav',rate, s1);


