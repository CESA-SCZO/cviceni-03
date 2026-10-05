import numpy as np
from numpy.fft import fft2, ifft2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from skimage.io import imread 

plt.close('all')

# Ukol 1
# =============================================================================
# Načtěte obraz „sports.jpg“
# Vyfiltrujte impulsní charakteristikou pomocí konvoluce v režimech 'valid', 'same' a 'full' a pozorujte výsledné rozdíly
# =============================================================================
plt.close('all')

img = imread('data/sports.jpg')
n = 51
h=np.zeros([n,n])
middle = int(n/2)
h[middle,middle] = 1


plt.figure()
plt.subplot(1,4,1)
plt.imshow(img, cmap = 'gray')
plt.title('Originalni obraz')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(..., cmap = 'gray')
plt.title('Vyfiltrovane v rezimu valid')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(...,  cmap = 'gray')
plt.title('Vyfiltrovane v rezimu same')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(...,  cmap = 'gray')
plt.title('Vyfiltrovane v rezimu full')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.show()

# Ukol 2
# =============================================================================
# Načtěte obraz „sports.jpg“
# Filtrujte obraz impulsní charakteristikou přes frekvenční oblast 
# =============================================================================
plt.close('all')
img = imread('data/sports.jpg')


plt.figure()
plt.subplot(1,3,1)
plt.imshow(img, cmap = 'gray')
plt.title('Originalni obraz')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(..., cmap = 'gray')
plt.title('Filtrovany pres frekvencni oblast')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(..., cmap = 'gray')
plt.title('Filtrovany konvoluci')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.axis('off')

plt.show()

