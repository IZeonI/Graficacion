# Creación de una imagen usando las primitivas de dibujo de OpenCV
~~~
import cv2 as cv

import numpy as np

  

#Se crea una imagen en blanco de 500x500 pixeles

img=np.ones((500,500), dtype=np.uint8)*255

  

#Se generan formas de dibujo basicas para crear una imagen en base a la poca creatividad del alumnno

cv.rectangle(img,(250,250),(500,500),(0,23,255),-1)

  
  

cv.circle(img,(0,0),50,(0,234,21), -1)

cv.line(img,(20,20),(250,250),(0,234,21), 2)

cv.rectangle(img,(0,0),(250,250),(0,234,21),3)

cv.circle(img,(250,250),30,(0,234,21), -1)

  

cv.circle(img,(500,500),50,(255,254,21), -1)

cv.line(img,(500,500),(250,250),(255,254,21), 2)

cv.rectangle(img,(500,500),(250,250),(255,254,21),3)

cv.rectangle(img,(250,250),(0,500),(0,23,255),-1)

  

cv.circle(img,(250,250),10,(250,254,21), -1)

  

#Se muestra el resultado de los 3 pesos de creatividad

cv.imshow('Intento de imagen creativa',img)

cv.waitKey(0)

cv.destroyAllWindows()
~~~
