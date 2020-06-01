import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import wsf


samplerate, data = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_scr_2.wav")
samplerate_old, data_old = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example.wav")
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

FFT_data = fft(data)


key = wsf.read_key_file("key.json")

data_descrambled = np.arange(0, data.shape[0], 1, dtype = "complex64")

for k in range(0, data.shape[0]):
    data_descrambled[key[k]] = data[k]

IFFT_data_scrambled = ifft(data_descrambled)

IFFT_data_scrambled = np.real(data_descrambled)

wavfile.write("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_descr_2.wav", 44100, IFFT_data_scrambled)

samplerate_descr, data_descr = wavfile.read("C:/Users/User/PycharmProjects/pazi_lab_1_final/example_descr_2.wav")

wsf.draw_compare_time_representation(t, data_old, data_descr, "Сравнение исходного и cкрэмблированного сигнала", "t", "A")