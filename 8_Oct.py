import cv2
import numpy as np

imagen = cv2.imread('salida.png', 1)


imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

rojo1=np.array([0,40,40])
rojo2=np.array([10,255,255])
rojo3=np.array([160,40,40])
rojo4=np.array([180,255,255])
amarillo1 = np.array([15, 40, 40])
amarillo2 = np.array([45, 255, 255])
verde1=np.array([40,40,40])
verde2=np.array([80,255,255])
azul1=np.array([85,40,40])
azul2=np.array([130,255,255])

mascara_rojo1=cv2.inRange(imagen_hsv,rojo1,rojo2)
mascara_rojo2=cv2.inRange(imagen_hsv,rojo3,rojo4)
mascara_rojo=cv2.add(mascara_rojo1,mascara_rojo2)
mascara_ama= cv2.inRange(imagen_hsv,amarillo1,amarillo2)
mascara_verde= cv2.inRange(imagen_hsv,verde1,verde2)
mascara_azul= cv2.inRange(imagen_hsv,azul1,azul2)

resultado_rojo=np.where(mascara_rojo[:,:,None]==255,imagen,imagen_gris_bgr)
resultado_ama = np.where(mascara_ama[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_verde = np.where(mascara_verde[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_azul = np.where(mascara_azul[:, :, None] == 255, imagen, imagen_gris_bgr)


cv2.imshow('Rojo', resultado_rojo)
cv2.imshow('Amarillo', resultado_ama)
cv2.imshow('Verde', resultado_verde)
cv2.imshow('Azul', resultado_azul)

cv2.waitKey(0)
cv2.destroyAllWindows()