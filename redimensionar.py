import cv2 as cv
import numpy as np

img=cv.imread('C:/Users/asewi/OneDrive/Documentos/bonk.jpeg',1)
x,y=img.shape
img2=np.zeros((x*2,y*2), dtype=np.uint8)
for i in range(x):
    for j in range(y):
        img2[i*2,j*2]=img[i,j]
        
cv.imshow('img',img)
cv.imshow('img2',img2)

cv.waitKey()
cv.destroyAllWindows()
