import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import random as rnd
import json
import wsf


samplerate, data = wavfile.read("C:/Users/User/PycharmProjects/PAZI_lab_1/wav/freq_swap_example.wav")
samplerate_old, data_old = wavfile.read("C:/Users/User/PycharmProjects/PAZI_lab_1/wav/test_2.wav")
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

#wsf.draw_time_representation(t, data, "График скрэмблированного сигнала", "t", "Ui")

FFT_data = fft(data)
#wsf.draw_spectrum_representation(f, 2*np.abs(FFT_data)/data.shape[0], "Спектр скрэмблированного сигнала", "f", "spectrum")


key = wsf.read_key_file("key.json")

data_descrambled = np.arange(0, data.shape[0], 1, dtype = "complex64")

for k in range(0, data.shape[0]):
    data_descrambled[key[k]] = data[k]
#
#
# wsf.draw_spectrum_representation(f, 2*np.abs(data_descrambled)/data.shape[0], "Cпектральное представление дескрэмблированного сигнала", "f", "spectrum")

IFFT_data_scrambled = ifft(data_descrambled)

#wsf.draw_compare_time_representation(t, data_old, np.real(IFFT_data_scrambled), "Сравнение исходного и cкрэмблированного сигнала", "t", "Ui")
IFFT_data_scrambled = np.real(data_descrambled)
wavfile.write("freq_swap_example_ifft.wav", 44100, IFFT_data_scrambled)

samplerate_descr, data_descr = wavfile.read("C:/Users/User/PycharmProjects/PAZI_lab_1/wav/freq_swap_example_ifft.wav")

wsf.draw_compare_time_representation(t, data_old, data_descr, "Сравнение исходного и cкрэмблированного сигнала", "t", "A")