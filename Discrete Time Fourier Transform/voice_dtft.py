##code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as wav

rate_a, data_a = wav.read('a.wav')
print(rate_a)

rate_i, data_i = wav.read('i.wav')
print(rate_i)

a=[1]
c=np.arange(0, np.pi, np.pi/496)

w1,h1=sig.freqz(data_a,a,c)
w2,h2=sig.freqz(data_i,a,c)

plt.plot(w1/(np.pi),abs(h1))
plt.show()
plt.plot(w2/(np.pi),abs(h2))
plt.show()

#i has higher frequency