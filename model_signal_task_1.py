import numpy as np
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

Ui = A[0]*np.cos(2*np.pi*F[0]*i*delta_t) + A[1]*np.cos(2*np.pi*F[1]*i*delta_t) + A[2]*np.cos(2*np.pi*F[2]*i*delta_t) + A[3]*np.cos(2*np.pi*F[3]*i*delta_t)

# draw time representation
msf.draw_time_representation(t, Ui, "Временное представление модельного сигнала", "t", "A")