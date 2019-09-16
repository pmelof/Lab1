# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.


# IMPORT LIBRARIES
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft
import scipy.io.wavfile as waves
import numpy as np


# FUNCTION DEFINITION
"""
Función que guarda el gráfico de la señal en el tiempo.
Entrada: arreglo de datos de la amplitud de la señal, frecuencia de muestreo, 
        nombre del grafico a guardar. 
Salida: sin variables de salida.
"""
def save_sound_graph(data_read, sample_rate, name):
    time = np.linspace(0, len(data_read) / sample_rate, num=len(data_read))
    plt.plot(time, data_read, color='y')
    plt.title('Amplitud v/s Tiempo', fontdict={'size': 15})
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.savefig(name, bbox_inches='tight')
    plt.clf()


"""
Función que guarda el gráfico de la señal en el dominio de la frecuencia y entrega
las transformadas de Fourier.
Entrada: arreglo de datos de la amplitud de la señal, frecuencia de muestreo.
Salida: transformada de Fourier discreta y frecuencias de muestra de Transformada 
        discreta de Fourier de la señal.
"""
def sound_freq_graph(data_read, sample_rate):
    fft_out = fft(data_read)
    fft_freq = fftfreq(len(data_read), 1 / sample_rate)
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido", fontdict={'size': 15})
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|F(w)|")
    plt.savefig("2 Grafico de la señal original en el dominio de la frecuencia.png", bbox_inches='tight')
    plt.clf()
    return fft_out, fft_freq


"""
Función que guarda el gráfico de la señal truncada en el dominio de la frecuencia y
los nuevos datos truncados de la transformada de Fourier.
Entrada: transformada de Fourier discreta, frecuencias de muestra de Transformada 
        discreta de Fourier de la señal.
Salida: transformada de Fourier discreta truncada.
"""
def truncated_sound_graph(fft_out, fft_freq):
    # centro 36556+-1
    fft_out[11346:61767] = 0
    plt.plot(fft_freq, np.abs(fft_out))
    plt.title("Transformada de Fourier \n del sonido (truncado)", fontdict={'size': 15})
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|F(w)|")
    plt.savefig("5 Grafico de la señal truncada en el dominio de la frecuencia.png", bbox_inches='tight')
    plt.clf()
    return fft_out


"""
Función que realiza la transformada de Fourier inversa y guarda la señal como un 
archivo de audio.
Entrada: datos de la señal, frecuencias de muestreo, nombre del archivo de salida.
Salida: transformada de Fourier inversa de la señal.
"""
def inverse_fft_to_sound_file(fft_out, sample_rate, file_name):
    ifft_out = ifft(fft_out)
    waves.write(file_name, sample_rate, ifft_out.real)
    return ifft_out


"""
Función bloque principal .
"""
def main():
    # Original Sound
    sample_rate, data_read = waves.read('handel.wav')
    save_sound_graph(data_read, sample_rate, "1 Grafico de la señal original en funcion del tiempo.png")

    # FFT and IFFT
    fft_out_1, fft_freq_1 = sound_freq_graph(data_read, sample_rate)
    ifft_out_1 = inverse_fft_to_sound_file(fft_out_1, sample_rate, 'hadel_inversa.wav')
    save_sound_graph(ifft_out_1.real, sample_rate, "3 Grafico de la señal reconstruida en funcion del tiempo.png")
    save_sound_graph(ifft_out_1.real - data_read, sample_rate, "4 Grafico de perdida de informacion al reconstruir la señal.png")

    # Truncated Sound and IFFT
    fft_out_2 = truncated_sound_graph(fft_out_1, fft_freq_1)
    ifft_out_2 = inverse_fft_to_sound_file(fft_out_2, sample_rate, 'hadel_truncado.wav')
    save_sound_graph(ifft_out_2.real, sample_rate, "6 Grafico de la señal truncada y reconstruida en funcion del tiempo.png")
    save_sound_graph(ifft_out_2.real - data_read, sample_rate, "7 Grafico de la perdida de informacion al reconstruir la señal truncada.png")


# CALL MAIN
main();
