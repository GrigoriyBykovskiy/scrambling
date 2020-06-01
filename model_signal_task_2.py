import numpy as np
from scipy.fftpack import fft, ifft
import msf
# default bandwidth
Fmin = 300
Fmax = 3400
# scrambling frequency
Fscr = 2*(Fmin+Fmax)
# sample count
N = 2048
# sample vector 0 .. (N-1)
i = np.arange(int(N))
# amplitude vector 1 .. 4
A = np.arange(1, 5)
# source frequency vector of harmonics 900 1400 1900 2400
F = np.arange(3 * Fmin, int(0.8 * Fmax), 500)
# time step
delta_t = 1 / (4*Fscr)
# time vector
t = i*delta_t
# freq step
delta_f = 1 / (delta_t*N)
# freq vector
f = i*delta_f


Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)

#make fft
FFT_Ui = fft(Ui)
# draw spectrum
msf.draw_spectrum_representation(f, 2*np.abs(FFT_Ui)/N, "Спектр модельного сигнала", "f", "spectrum")
#make ifft
IFFT_Ui = ifft(FFT_Ui)
# draw compare time representation
msf.draw_compare_time_representation(t, Ui, np.real(IFFT_Ui), "Модельный сигнал до и после преобразований", "t", "A")