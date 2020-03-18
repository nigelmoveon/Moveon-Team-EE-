import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift
import numpy as np

file = open('test.txt', 'r')
data = file.read()          # read all as txt
file.close()

data1 = fft(data.split())

data1 = [ float(x) for x in data1]

plt.plot(data1, 'r-')

plt.ylabel('mV')
plt.show()
