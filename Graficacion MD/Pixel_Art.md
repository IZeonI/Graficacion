# Pixel art usando una matriz de enteros de 0 a 255

~~~
import cv2 as cv

import numpy as np

  

#Se crea una imagen de 500x500 pixeles en color blanco

img=np.ones((500,500), dtype=np.uint8)*255

#Se obtiene el valor de x,y de img para usarlos despues

x,y=img.shape

  

#Se inicia un ciclo for anidado que recorre pixel por pixel de img

for i in range(x):

    for j in range(y):  

        #Se le da un valor aleatorio al pixel entre 0 y 255

        img[i, j] = np.random.randint(0,255)

  

#Se muestra el resultado de img despues del ciclo for        

cv.imshow("Pixel Art Aleatorio",img)

cv.waitKey(0)

cv.destroyAllWindows()
~~~
