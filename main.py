import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# default bandwidth
Fmin = 300
Fmax = 3400
# sample count
N = 1024
# sample vector 0 .. (N-1)
i = np.arange(float(N))
# amplitude vector 0 .. 4
A = np.arange(1, 5)
# source frequency vector of harmonics 600 1400 2200 3000
F = np.arange(2*Fmin, Fmax, 800)
# time step
delta_t = 1 / (2 * (Fmin + Fmax))

Ui = Ui = np.cos(2*np.pi*400*i*delta_t) + 2*np.cos(2*np.pi*950*i*delta_t) + 3*np.cos(2*np.pi*1325*i*delta_t)

# Select: plot, stem, bar
def plt_sel(s, *args, **kwargs):
    if s == 0:
        return plt.plot(*args)
    if s == 1:
        return plt.stem(*args, **kwargs)
    if s == 2:
        return plt.step(*args)


# Subplot titles
t_titles = ['Аналоговый', 'Дискретный', 'Квантованный']

# Plot figures
fig = plt.figure(figsize=(16, 4), dpi=80)
for k in range(3):
    plt.subplot(1, 3, k + 1)
    plt.title(t_titles[k])
    plt_sel(k, i, Ui, use_line_collection=True)
    plt.xlim([0, 50])
    plt.yticks(np.linspace(np.floor(np.min(Ui)), np.ceil(np.max(Ui)), 9))
    plt.grid(True)

    # change plot view
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
plt.tight_layout()
plt.show()