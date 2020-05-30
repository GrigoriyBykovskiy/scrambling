import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import math


def draw_time_representation (x, y, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y, color='red', linestyle='-', linewidth=1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xlim([np.min(x), x[200]])
    ax.set_ylim(math.ceil(np.min(y)) - 1, math.ceil(np.max(y)) + 1)

    ax.grid(which='major',
            color='black',
            linewidth=1)

    ax.minorticks_on()

    ax.grid(which='minor',
            color='gray',
            linestyle=':')

    fig.tight_layout()
    plt.show()


def draw_compare_time_representation(x, y1, y2, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y1, color='red', linestyle='-', linewidth=1)
    ax.plot(x, y2, color='green', linestyle=':', linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xlim([np.min(x), x[200]])
    ax.set_ylim(math.ceil(np.min(y1)) - 1, math.ceil(np.max(y1)) + 1)

    ax.grid(which='major',
            color='black',
            linewidth=1)

    ax.minorticks_on()

    ax.grid(which='minor',
            color='gray',
            linestyle=':')

    fig.tight_layout()
    plt.show()


def draw_spectrum_representation(x, y, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y, color='red', linestyle='-', linewidth=0.5)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xlim([np.min(x), np.max(x)])
    ax.set_ylim(math.ceil(np.min(y))-1, math.ceil(np.max(y))+1)

    ax.grid(which='major',
            color='black',
            linewidth=1)

    ax.minorticks_on()

    ax.grid(which='minor',
            color='gray',
            linestyle=':')

    fig.tight_layout()
    plt.show()


def get_filtered_spectrum(fscr, n, delta_f, f, x):
    filtered_x = x
    filter_min, = np.where(f == int(fscr))
    filter_max, = np.where(f == int(n * delta_f - fscr))

    for i in range(filter_min[0], filter_max[0]):
        filtered_x[i] = 0

    return filtered_x


def main():
    print("\nANTA BAKA?!\nIt is file for functions\n")


if __name__ == "__main__":
    main()
