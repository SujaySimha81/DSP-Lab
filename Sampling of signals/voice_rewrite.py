import numpy as np 
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

rate, data = wav.read('aceright.wav',mmap=False)
print(rate)
print(data)
wav.write('voice.wav',8000,data)
print(np.mean(data))
print(np.var(data))