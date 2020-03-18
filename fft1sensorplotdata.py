import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
import numpy as np

	
file = open('log.txt', 'r')
data = file.read()          # read all as txt
file.close()

timestep = 0.001

data = data.split()
data = [ float(x) for x in data]
datafft = np.fft.rfft(data)
power = np.abs(datafft)
samplefreq = np.fft.rfftfreq(len(data),d=timestep)
#mask = samplefreq > 0
order = np.argsort(samplefreq)
#data1 = [ float(x) for x in data1]

# pos_mask = np.where(samplefreq > 0)
# freqs = samplefreq[pos_mask]
# #peak_freq = freqs[power[pos_mask].argmax()]

# high_freq_fft = datafft.copy()
# high_freq_fft[np.abs(samplefreq) > 250] = 0
# filteredsig = np.fft.ifft(high_freq_fft)



plt.figure("FFT filter")
plt.subplot(211)
#plt.plot(samplefreq[order], power[order], 'r-')
#plt.plot(data, 'r-')
plt.plot(samplefreq, power, 'r-')
#plt.plot(datafft)


sf = 1000
cutoff = 200
nyq = 0.5 * len(data)
N = 1
fc = cutoff / nyq
b, a = signal.butter(N, fc)
y = signal.filtfilt(b, a, data)

plt.subplot(212)
plt.xlabel('Data point')
plt.ylabel('adc value')
plt.plot(y)


# plt.figure("FFT filter")
# plt.xlabel('Data point')
# plt.ylabel('adc value')
# plt.plot(filteredsig,'b-')




#plt.ylabel('mV')
plt.show()
