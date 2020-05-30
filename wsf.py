import numpy as np
import matplotlib.pyplot as plt
import json


def draw_time_representation (x, y, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y, color='red', linestyle='-', linewidth=1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(y), np.max(y))

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
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(y1), np.max(y1))

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
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(y), np.max(y))

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


def generate_key(low, high, step):
    key = np.arange(low, high, step)
    np.random.shuffle(key)
    return key


def write_key_file(filename, key):
    with open(filename, "w") as write_file:
        json.dump(key.tolist(), write_file)
    write_file.close()


def read_key_file(filename):
    with open(filename, "r") as read_file:
        read_key = json.load(read_file)
    read_file.close()
    return read_key


def main():
    print("\nANTA BAKA?!\nIt is file for functions\n")


if __name__ == "__main__":
    main()
