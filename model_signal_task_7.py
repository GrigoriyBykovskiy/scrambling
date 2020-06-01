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
# scrambling signal
SCR = np.cos(2*np.pi*Fscr*i*delta_t)
# model signal
Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)

# find summary signal
Ui_sum = Ui*SCR
# make fft
FFT_Ui_sum = fft(Ui_sum)
# filtering signal
FFT_Ui_filtered = msf.get_filtered_spectrum(Fscr, N, delta_f, f, FFT_Ui_sum)
# make ifft
IFFT_FFT_Ui_filtered = ifft(FFT_Ui_filtered)

#msf.draw_compare_time_representation(t, Ui, np.real(IFFT_FFT_Ui_filtered), "Сравнение исходного и скрэмблированного модельного сигнала", "t", "A")

# if fi not null
SCR = np.cos(2*np.pi*Fscr*i*delta_t - 1.5*np.pi)
# find descrambling signal
DSCR = IFFT_FFT_Ui_filtered*SCR
# make fft
FFT_DSCR = fft(DSCR)
#msf.draw_spectrum_representation(f, 2*np.abs(FFT_DSCR)/N, "Спектр дескрэмблированного сигнала", "f", "spectrum")

FFT_DSCR_filtered = msf.get_filtered_spectrum(Fscr, N, delta_f, f, FFT_DSCR)
#msf.draw_spectrum_representation(f, 2*np.abs(FFT_DSCR_filtered)/N, "Спектр дескрэмблированного сигнала после фильтрации", "f", "spectrum")

# make ifft
FFT_DSCR_Ui_filtered = ifft(FFT_DSCR_filtered)

msf.draw_compare_time_representation(t, Ui, np.real(FFT_DSCR_Ui_filtered), "Сравнение исходного и дескрэмблированного модельного сигнала", "t", "A")