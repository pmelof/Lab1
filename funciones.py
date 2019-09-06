# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.
# Versión 1.


# IMPORTAR LIRERÍAS
import matplotlib.pylab as plt
import scipy as sp
import scipy.io.wavfile as waves
import wave
import numpy as np

# DEFINICIÓN DE CONSTANTES

# DEFINICIÓN DE FUNCIONES
def graphSong(dataRead, sampleRate):
    time = np.linspace(0, len(dataRead) / sampleRate, num=len(dataRead))
    plt.plot(time, dataRead, color='y')
    plt.title('Amplitud v/s Tiempo', fontdict={'size': 15})
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()

def main():
    sampleRate, dataRead = waves.read('handel.wav')
    graphSong(dataRead, sampleRate)

# INGRESO
main();