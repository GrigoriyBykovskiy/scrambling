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

fig, ax = plt.subplots(figsize=(10, 10))
# analog
ax.plot(i, Ui, color='red', linestyle='-', linewidth=1)
# discrete in time continuous in magnitude
# ax.stem(i, Ui, linefmt=None, markerfmt=None, basefmt=None, use_line_collection=True)
ax.set_title('Аналоговое представление модельного сигнала')
ax.set_xlabel('i')
ax.set_ylabel('Ui')
ax.set_xlim([np.min(i), i[100]])
ax.set_ylim(math.ceil(np.min(Ui))-1, math.ceil(np.max(Ui))+1)

ax.grid(which='major',
        color = 'black',
        linewidth = 1)

ax.minorticks_on()

ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.tight_layout()
plt.show()