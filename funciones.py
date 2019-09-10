# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.
# Versión 1.


# IMPORTAR LIRERÍAS
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy import fftpack
import scipy as sp
import scipy.io.wavfile as waves
import wave
import numpy as np

# DEFINICIÓN DE CONSTANTES

# DEFINICIÓN DE FUNCIONES
def graphSong(data_read, sample_rate):
    time = np.linspace(0, len(data_read) / sample_rate, num=len(data_read))
    plt.plot(time, data_read, color='y')
    plt.title('Amplitud v/s Tiempo', fontdict={'size': 15})
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()


def fftGraphSong(data_read, sample_rate):
    fft_out = fft(data_read)
    fft_freq = fftfreq(len(data_read), 1/sample_rate)
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier de la canción")
    plt.xlabel("Frecuencia")
    plt.ylabel("|F(w)|")
    plt.show()
    truncateGraphSong(fft_out, fft_freq, sample_rate)


def invFftFileSong(fft_out, sample_rate, name_file):
    ifft_out = ifft(fft_out)
    plt.plot(ifft_out.real)
    plt.show()
    waves.write(name_file, sample_rate, ifft_out.real)


def truncateGraphSong(fft_out, fft_freq, sample_rate):
    #centro 36556+-1
    fft_out[16556:56557] = 0
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier de la canción (truncado)")
    plt.xlabel("Frecuencia")
    plt.ylabel("|F(w)|")
    plt.show()
    invFftFileSong(fft_out, sample_rate, 'truncado.wav')


def main():
    sample_rate, data_read = waves.read('handel.wav')
    #print(sample_rate)
    #print(len(data_read))
    graphSong(data_read, sample_rate)
    fftGraphSong(data_read, sample_rate)



# INGRESO
main();