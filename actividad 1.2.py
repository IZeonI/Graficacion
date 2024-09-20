import cv2 as cv
import numpy as np
import math

img=cv.imread('C:/Users/asewi/OneDrive/Documentos/waos.png',0)

x,y=img.shape
rotated_img=np.zeros((x*2,y*2), dtype=np.uint8)
cx,cy=int(x//2),int(y//2)

angle=30
angle2=60
theta=math.radians(angle)
iota=math.radians(angle2)

for i in range(x):
    for j in range(y):
        new_x=int(((j-cx)*math.cos(theta)-(i-cy)*math.sin(theta)+cx) * ((j-cx)*math.cos(iota)+(i-cy)*math.sin(iota)+cx))
        new_y=int(((j-cx)*math.sin(theta)+(i-cy)*math.cos(theta)+cy) * (-(j-cx)*math.sin(iota)+(i-cy)*math.cos(iota)+cy))
        if 0<=new_x < y and 0<=new_y<x:
            rotated_img[new_y , new_x]=img[i,j]
            
cv.imshow('IMAGEN ORIGINAL',img)
cv.imshow('IMAGEN ROTADA(MODO RAW)',rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()
