import cv2 as cv
import numpy as np

img=cv.imread('bonk.jpeg',0)
x,y=img.shape
scala_x,scala_y= 2,2
img_escalada=np.zeros((int(x*scala_x),int(y*scala_y)), dtype=np.uint8)
img_convolucion=np.zeros((int(x*scala_x),int(y*scala_y)), dtype=np.uint8)

for i in range(x):
    for j in range(y):
        img_escalada[i*scala_x,j*scala_y]=img[i,j]
        img_convolucion[i*scala_x,j*scala_y]=img[i,j]
        
for i in range(x*scala_x-1):
    for j in range(y*scala_y-1):
            img_convolucion[i,j]=int((1/9)*(
                img_escalada[i-1,j-1]+img_escalada[i,j-1]+img_escalada[i+1,j-1]+
                img_escalada[i-1,j]+img_convolucion[i,j]+img_escalada[i+1,j]+
                img_escalada[i-1,j+1]+img_escalada[i,j+1]+img_escalada[i+1,j+1]))
 
        
cv.imshow('img',img)
cv.imshow('imagen escalada',img_escalada)
cv.imshow('imagen convolucionada',img_convolucion)
cv.waitKey()
cv.destroyAllWindows()