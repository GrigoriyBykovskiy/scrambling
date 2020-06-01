import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import wsf


samplerate, data = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_scr.wav")
length = data.shape[0] / samplerate
# sample vector 0 .. (N-1)
i = np.arange(int(data.shape[0]))
# time step
delta_t = 1 / samplerate
# time vector
t = i*delta_t
# freq step
delta_f = 1 / (int(data.shape[0])*delta_t)
# freq vector
f = i*delta_f
# scrambling frequency
Fscr = 1 / (4*delta_t)

# scrambling signal
SCRi = np.cos(2*np.pi*float(Fscr)*i*delta_t)

# find summary signal
data_sum = data*SCRi

# make fft
FFT_data_sum = fft(data_sum)
wsf.draw_spectrum_representation(f, 2*np.abs(FFT_data_sum)/data.shape[0], "Спектр дескрэмблированного сигнала", "f", "spectrum")

FFT_data_sum_filtered = wsf.get_filtered_spectrum(Fscr, data.shape[0], delta_f, f, FFT_data_sum)

wsf.draw_spectrum_representation(f, 2*np.abs(FFT_data_sum_filtered)/data.shape[0], "Спектр дескрэмблированного сигнала отфильтрованный", "f", "spectrum")

IFFT_FFT_Ui_filtered = ifft(FFT_data_sum_filtered)

wsf.draw_compare_time_representation(t, data, np.real(IFFT_FFT_Ui_filtered), "Сравнение исходного и дескрэмблированного сигнала", "t", "A")

IFFT_FFT_Ui_filtered = 4*np.real(IFFT_FFT_Ui_filtered)
wavfile.write("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_descr.wav", 44100, IFFT_FFT_Ui_filtered)