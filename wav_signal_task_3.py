import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import wsf


samplerate, data = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example.wav")
length = data.shape[0] / samplerate
# sample vector 0 .. (N-1)
i = np.arange(int(data.shape[0]))
# time step
delta_t = 1 / samplerate
# time vector
t = i*delta_t
# freq step
delta_f = 1 / (data.shape[0]*delta_t)
# freq vector
f = i*delta_f

wsf.draw_time_representation(t, data, "График исходного сигнала", "t", "A")

FFT_data = fft(data)

key = wsf.generate_key(0, data.shape[0], 1)
wsf.write_key_file("key.json", key)

data_scrambled = np.arange(0, data.shape[0], 1, dtype="complex64")
for k in range(0, data.shape[0]):
    data_scrambled[k] = data[key[k]]

IFFT_data_scrambled = ifft(data_scrambled)

IFFT_data_scrambled = np.real(data_scrambled)
wavfile.write("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_scr_2.wav", 44100, IFFT_data_scrambled)

samplerate_scr, data_scr = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_scr_2.wav")

wsf.draw_compare_time_representation(t, data, data_scr, "Сравнение исходного и cкрэмблированного сигнала", "t", "A")