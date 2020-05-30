import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import wsf


samplerate, data = wavfile.read("C:/Users/User/PycharmProjects/PAZI_lab_1/wav/test_2.wav")
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

#wsf.draw_spectrum_representation(f, 2*np.abs(FFT_data)/data.shape[0], "Спектр исходного сигнала", "f", "spectrum")

key = wsf.generate_key(0, data.shape[0], 1)
wsf.write_key_file("key.json", key)

data_scrambled = np.arange(0, data.shape[0], 1, dtype="complex64")
for k in range(0, data.shape[0]):
    data_scrambled[k] = data[key[k]]

#wsf.draw_spectrum_representation(f, np.abs(data_scrambled), "Cпектральное представление скрэмблированного сигнала", "f", "spectrum")
#wsf.draw_spectrum_representation(f, 2*np.abs(data_scrambled)/data_scrambled.shape[0], "Cпектральное представление скрэмблированного сигнала", "f", "spectrum")

IFFT_data_scrambled = ifft(data_scrambled)

#wsf.draw_time_representation(t, IFFT_data_scrambled, "График скрэмблированного сигнала", "t", "A")
#wsf.draw_compare_time_representation(t, data, np.real(IFFT_data_scrambled), "Сравнение исходного и cкрэмблированного сигнала", "t", "A")
IFFT_data_scrambled = np.real(data_scrambled)
wavfile.write("freq_swap_example.wav", 44100, IFFT_data_scrambled)

samplerate_scr, data_scr = wavfile.read("C:/Users/User/PycharmProjects/PAZI_lab_1/wav/freq_swap_example.wav")

wsf.draw_compare_time_representation(t, data, data_scr, "Сравнение исходного и cкрэмблированного сигнала", "t", "A")

