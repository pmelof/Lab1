# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.


# IMPORT LIBRARIES
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
import scipy.io.wavfile as waves
import numpy as np


# FUNCTION DEFINITION
def save_sound_graph(data_read, sample_rate, name):
    time = np.linspace(0, len(data_read) / sample_rate, num=len(data_read))
    plt.plot(time, data_read, color='y')
    plt.title('Amplitud v/s Tiempo', fontdict={'size': 15})
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.savefig(name, bbox_inches='tight')
    plt.show()


def sound_freq_graph(data_read, sample_rate):
    fft_out = fft(data_read)
    fft_freq = fftfreq(len(data_read), 1 / sample_rate)
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido", fontdict={'size': 15})
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|F(w)|")
    plt.savefig("2 Transformada de Fourier.png", bbox_inches='tight')
    plt.show()
    return fft_out, fft_freq


def truncated_sound_graph(fft_out, fft_freq):
    # centro 36556+-1
    fft_out[11346:61767] = 0
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido (truncado)", fontdict={'size': 15})
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|F(w)|")
    plt.savefig("5 Transformada de Fourier (truncada).png", bbox_inches='tight')
    plt.show()
    return fft_out


def inverse_fft_to_sound_file(fft_out, sample_rate, file_name):
    ifft_out = ifft(fft_out)
    waves.write(file_name, sample_rate, ifft_out.real)
    return ifft_out


def main():
    # Original Sound
    sample_rate, data_read = waves.read('handel.wav')
    save_sound_graph(data_read, sample_rate, "1 Amplitud vs Tiempo (original).png")

    # FFT and IFFT
    fft_out_1, fft_freq_1 = sound_freq_graph(data_read, sample_rate)
    ifft_out_1 = inverse_fft_to_sound_file(fft_out_1, sample_rate, 'inversa.wav')
    save_sound_graph(ifft_out_1.real, sample_rate, "3 Amplitud vs Tiempo (inversa).png")
    save_sound_graph(ifft_out_1.real - data_read, sample_rate, "4 Amplitud vs Tiempo (dif original inversa).png")

    # Truncated Sound and IFFT
    fft_out_2 = truncated_sound_graph(fft_out_1, fft_freq_1)
    ifft_out_2 = inverse_fft_to_sound_file(fft_out_2, sample_rate, 'truncado.wav')
    save_sound_graph(ifft_out_2.real, sample_rate, "6 Amplitud vs Tiempo (truncado).png")
    save_sound_graph(ifft_out_2.real - data_read, sample_rate, "7 Amplitud vs Tiempo (dif original truncado).png")


# CALL MAIN
main();
