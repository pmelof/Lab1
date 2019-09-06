# Universidad de Santiago de Chile
# Laboratorio 1 de Redes de Computadores
# Autores: Williams Álvarez y Patricia Melo.
# Versión 1.


# IMPORTAR LIRERÍAS
import matplotlib.pylab as plt
import scipy as sp
import scipy.io.wavfile as waves
import numpy as np

# DEFINICIÓN DE CONSTANTES

# DEFINICIÓN DE FUNCIONES

# INGRESO

muestreo, sonido = waves.read('handel.wav')

plt.plot(sonido)
plt.title('Sonido')
plt.xlabel('Tiempo [s]')
plt.ylabel('Algo')
plt.show()

print("hola")