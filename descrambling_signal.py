import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math
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
# source frequency vector of harmonics 600 1400 2200 3000
F = np.arange(2*Fmin, Fmax, 800)
# time step
delta_t = 1 / (4*Fscr)
# freq step
delta_f = 1 / (N*delta_t)
# freq vector
f = i*delta_f
# time vector
t = i*delta_t

# model signal
Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)

# scrambling signal
SCRi = np.cos(2*np.pi*float(Fscr)*i*delta_t)

# find summary signal
Ui_sum = Ui*SCRi

# make fft
FFT_Ui = fft(Ui_sum)
msf.draw_spectrum_representation(f, 2*np.abs(FFT_Ui)/N, "Спектр скрэмблированного сигнала", "f", "spectrum")
# draw spectrum of scrambled signal
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(f, FFT_Ui, color='red', linestyle='-', linewidth=0.5)
# ax.set_title('Спектр скрэмблированного сигнала')
# ax.set_xlabel('f')
# ax.set_xlim([np.min(f), np.max(f)])
# ax.set_ylim(math.ceil(np.min(FFT_Ui))-1, math.ceil(np.max(FFT_Ui))+1)
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()
FFT_Ui_filtered = msf.get_filtered_spectrum(Fscr, N, delta_f, f, FFT_Ui)
# filtered spectrum of scrambled signal
# filter_min, = np.where(f == int(Fscr))
# filter_max, = np.where(f == int(N*delta_f - Fscr))
#
# FFT_Ui_filtered = FFT_Ui
#
# for i in range(filter_min[0], filter_max[0]):
#     FFT_Ui_filtered[i] = FFT_Ui_filtered[0]
msf.draw_spectrum_representation(f, 2*np.abs(FFT_Ui_filtered)/N, "Спектр скрэмблированного сигнала после фильтрации", "f", "spectrum")
# draw spectrum of filtered scrambled signal
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(f, FFT_Ui_filtered, color='red', linestyle='-', linewidth=0.5)
# ax.set_title('Спектр скрэмблированного сигнала после применения фильтра')
# ax.set_xlabel('f')
# ax.set_xlim([np.min(f), np.max(f)])
# ax.set_ylim(math.ceil(np.min(FFT_Ui_filtered))-1, math.ceil(np.max(FFT_Ui_filtered))+1)
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()

# make ifft
IFFT_FFT_Ui_filtered = ifft(FFT_Ui_filtered)

msf.draw_compare_time_representation(t, Ui, np.real(IFFT_FFT_Ui_filtered), "Сравнение исходного и скрэмблированного модельного сигнала", "t", "Ui")
# draw
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(t, IFFT_FFT_Ui_filtered, color='red', linestyle=':', linewidth=1)
# ax.plot(t, Ui, color='green', linestyle='-', linewidth=1)
# ax.set_title('Сравнение исходного и скрэмблированного модельного сигнала ')
# ax.set_xlabel('t')
# ax.set_ylabel('Ui')
# ax.set_xlim([np.min(t), t[200]])
# ax.set_ylim(math.ceil(np.min(IFFT_FFT_Ui_filtered))-1, math.ceil(np.max(IFFT_FFT_Ui_filtered))+1)
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()

# find descrambling signal
DSCR_Ui = IFFT_FFT_Ui_filtered*SCRi
# make fft
FFT_DSCR_Ui = fft(DSCR_Ui)
msf.draw_spectrum_representation(f, 2*np.abs(FFT_DSCR_Ui)/N, "Спектр дескрэмблированного сигнала", "f", "spectrum")
# draw spectrum of descrambled signal
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(f, np.abs(FFT_DSCR_Ui), color='red', linestyle='-', linewidth=0.5)
# ax.set_title('Спектр дескрэмблированного сигнала')
# ax.set_xlabel('f')
# ax.set_xlim([np.min(f), np.max(f)])
# ax.set_ylim(math.ceil(np.min(FFT_DSCR_Ui))-1, math.ceil(np.max(FFT_DSCR_Ui))+1)
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()
FFT_DSCR_Ui_filtered = msf.get_filtered_spectrum(Fscr, N, delta_f, f, FFT_DSCR_Ui)
msf.draw_spectrum_representation(f, 2*np.abs(FFT_DSCR_Ui_filtered)/N, "Спектр дескрэмблированного сигнала после фильтрации", "f", "spectrum")
# filtered spectrum of descrambled signal
# filter_min, = np.where(f == int(Fscr))
# filter_max, = np.where(f == int(N*delta_f - Fscr))
#
# FFT_DSCR_Ui_filtered = FFT_DSCR_Ui
#
# for i in range(filter_min[0], filter_max[0]):
#     FFT_DSCR_Ui_filtered[i] = 0

# draw spectrum of descrambled signal
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(f, np.real(FFT_DSCR_Ui_filtered) , color='red', linestyle='-', linewidth=0.5)
# ax.set_title('Спектр дескрэмблированного сигнала после фильтрации')
# ax.set_xlabel('f')
# ax.set_xlim([np.min(f), np.max(f)])
# ax.set_ylim(math.ceil(np.min(np.real(FFT_DSCR_Ui_filtered)))-1, math.ceil(np.max(np.real(FFT_DSCR_Ui_filtered))+1))
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()

# make ifft
FFT_DSCR_Ui_filtered = ifft(FFT_DSCR_Ui_filtered)

msf.draw_compare_time_representation(t, Ui, np.real(FFT_DSCR_Ui_filtered), "Сравнение исходного и дескрэмблированного модельного сигнала", "t", "Ui")
# draw
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(t, FFT_DSCR_Ui_filtered, color='red', linestyle=':', linewidth=1)
# ax.plot(t, Ui, color='green', linestyle='-', linewidth=1)
# ax.set_title('Сравнение исходного и дескрэмблированного модельного сигнала ')
# ax.set_xlabel('t')
# ax.set_ylabel('Ui')
# ax.set_xlim([np.min(t), t[200]])
# ax.set_ylim(math.ceil(np.min(Ui))-1, math.ceil(np.max(Ui))+1)
#
# ax.grid(which='major',
#         color = 'black',
#         linewidth = 1)
#
# ax.minorticks_on()
#
# ax.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')
#
# fig.tight_layout()
# plt.show()