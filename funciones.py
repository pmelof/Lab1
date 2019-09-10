# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.


# IMPORT LIBRARIES
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
import scipy.io.wavfile as waves
import numpy as np


# FUNCTION DEFINITION
def sound_graph(data_read, sample_rate):
    time = np.linspace(0, len(data_read) / sample_rate, num=len(data_read))
    plt.plot(time, data_read, color='y')
    plt.title('Amplitud v/s Tiempo', fontdict={'size': 15})
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()


def sound_freq_graph(data_read, sample_rate):
    fft_out = fft(data_read)
    fft_freq = fftfreq(len(data_read), 1 / sample_rate)
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido", fontdict={'size': 15})
    plt.xlabel("Frecuencia")
    plt.ylabel("|F(w)|")
    plt.show()
    return fft_out, fft_freq


def truncated_sound_graph(fft_out, fft_freq):
    # centro 36556+-1
    fft_out[11346:61767] = 0
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido (truncado)", fontdict={'size': 15})
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|F(w)|")
    plt.show()
    return fft_out


def inverse_fft_to_sound_file(fft_out, sample_rate, file_name):
    ifft_out = ifft(fft_out)
    waves.write(file_name, sample_rate, ifft_out.real)
    return ifft_out


def main():
    # Original Sound
    sample_rate, data_read = waves.read('handel.wav')
    sound_graph(data_read, sample_rate)

    # FFT and IFFT
    fft_out_1, fft_freq_1 = sound_freq_graph(data_read, sample_rate)
    ifft_out_1 = inverse_fft_to_sound_file(fft_out_1, sample_rate, 'inversa.wav')
    sound_graph(ifft_out_1.real, sample_rate)

    # Truncated Sound and IFFT
    fft_out_2 = truncated_sound_graph(fft_out_1, fft_freq_1)
    ifft_out_2 = inverse_fft_to_sound_file(fft_out_2, sample_rate, 'truncado.wav')
    sound_graph(ifft_out_2.real, sample_rate)


# CALL MAIN
main();
