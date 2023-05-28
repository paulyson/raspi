import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.loadtxt(sys.argv[1], delimiter=',', skiprows=1, usecols=(0,1,2))
plt.plot(data[:,0])
plt.show()
plt.plot(data[:,1])
plt.show()
plt.plot(data[:,2])
plt.show()

fft_temp = np.abs(np.fft.fft(data[:,0]))
print(len(fft_temp))
plt.plot(fft_temp[1:len(fft_temp)/2])
plt.show()
