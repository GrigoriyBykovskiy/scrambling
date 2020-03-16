import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import math
# default bandwidth
Fmin = 300
Fmax = 3400
# sample count
N = 10000
# sample vector 0 .. (N-1)
i = np.arange(int(N))
# amplitude vector 0 .. 4
A = np.arange(1, 5)
# source frequency vector of harmonics 600 1400 2200 3000
F = np.arange(2*Fmin, Fmax, 800)
# time step
delta_t = 1 / N

# Ui = np.cos(2*np.pi*400*i*delta_t) + 2*np.cos(2*np.pi*950*i*delta_t) + 3*np.cos(2*np.pi*1325*i*delta_t)
Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)
#make fft
S = fft(Ui)
S = 2*np.abs(S) / N

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(i, S, color='red', marker='o', linestyle='-', linewidth=0.5)
ax.set_title('Спектр модельного сигнала')
ax.set_xlabel('i')
ax.set_xlim([np.min(i), np.max(i)])
ax.set_ylim(math.ceil(np.min(S))-1, math.ceil(np.max(S))+1)

ax.grid(which='major',
        color = 'black',
        linewidth = 1)

ax.minorticks_on()

ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.tight_layout()
plt.show()
