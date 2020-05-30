import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import math
# default bandwidth
Fmin = 300
Fmax = 3400
# scrambling frequency
Fscr = 1.5*(Fmin+Fmax)
# sample count
N = 2048
# sample vector 0 .. (N-1)
i = np.arange(int(N))
# amplitude vector 0 .. 4
A = np.arange(1, 5)
# source frequency vector of harmonics 600 1400 2200 3000
F = np.arange(2*Fmin, Fmax, 800)
# time step
delta_t = 1 / (4*Fscr)
# freq step
delta_f = 1 / (delta_t*N)
# freq vector
f = i*delta_f
# scrambling frequency vector
F_scr_i = np.cos(2*np.pi*2*(Fmin+Fmax)*i*delta_t)

# Ui = np.cos(2*np.pi*400*i*delta_t) + 2*np.cos(2*np.pi*950*i*delta_t) + 3*np.cos(2*np.pi*1325*i*delta_t)
Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)

# find summary signal
Ui_sum = Ui*F_scr_i

#make fft
Ui_scr = fft(Ui_sum)
Ui_scr = 2 * np.abs(Ui_scr) / N

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(f, Ui_scr, color='red', linestyle='-', linewidth=0.5)
ax.set_title('Спектр модельного сигнала')
ax.set_xlabel('i*delta_f')
ax.set_xlim([np.min(f), np.max(f)])
ax.set_ylim(math.ceil(np.min(Ui_scr))-1, math.ceil(np.max(Ui_scr))+1)

ax.grid(which='major',
        color = 'black',
        linewidth = 1)

ax.minorticks_on()

ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.tight_layout()
plt.show()