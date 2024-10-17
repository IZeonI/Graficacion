# Generación de 5 operadores puntuales
~~~
import cv2 as cv

import numpy as np

  

#Se importa una imagen a color en 2 variables diferentes

img2=cv.imread('bonk.jpeg', 1)

img = cv.imread('bonk.jpeg', 1)

#Se obtiene el valor de x,y,z de img

x,y,z=img.shape

  

#Se inicia un ciclo anidado for para recorrer cada pixel de img

for i in range(x):

    for j in range(y):

        #Se define una variable aleatoria que da valores de 1-5

        random=np.random.randint(1,6)

        #Se simula un switch, que en cada caso de 1-5 utiliza un operador puntual diferente

        if random == 1:

            img[i,j]=[0,0,0]

        elif random == 2:

            img[i,j]=[255,255,255]

        elif random == 3:

            img[i,j]=[35,255,0]

        elif random == 4:

            img[i,j]=[255,0,70]

        elif random == 5:

            img[i,j]=[224,0,255]

  

#Se muestra el resultado antes y despues de aplicar los operadores

cv.imshow('Antes de operadores', img2)

cv.imshow('Despues de operadores', img)

cv.waitKey(0)

cv.destroyAllWindows()
~~~
