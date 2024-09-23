import numpy as np
import cv2

def generar_punto_elipse(a, b, t):
    x = int(a * np.cos(t) + 300)  
    y = int(b * np.sin(t) + 300)
    return (x, y)

img_width, img_height = 600, 600
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

a = 200  
b = 100  
num_puntos = 100

t_vals = np.linspace(0, 2 * np.pi, num_puntos)


for t in t_vals:
    
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    
    # Generar el punto en la elipse
    punto00 = generar_punto_elipse(a-199, b-99, t)
    punto0 = generar_punto_elipse(a-150, b-60, t-3)
    punto = generar_punto_elipse(a, b, t)
    punto2 = generar_punto_elipse(a+30, b+30, t+5)
    punto3 = generar_punto_elipse(a+70, b+70, t+1)
    
    # Dibujar el punto en la elipse
    cv2.circle(imagen, punto00, radius=10, color=(100, 0, 255), thickness=-1)
    cv2.circle(imagen, punto0, radius=5, color=(100, 100, 150), thickness=-1)
    cv2.circle(imagen, punto, radius=5, color=(0, 200, 230), thickness=-1)
    cv2.circle(imagen, punto2, radius=10, color=(255, 0, 100), thickness=-1)
    cv2.circle(imagen, punto3, radius=15, color=(0, 255, 0), thickness=-1)
    
    # Dibujar la trayectoria completa de la elipse (opcional, si quieres ver toda la elipse)
    for t_tray in t_vals:
        pt_tray00 = generar_punto_elipse(a-199, b-99, t_tray)
        #cv2.circle(imagen, pt_tray00, radius=1, color=(255, 255, 255), thickness=-1) elipse del sol
        pt_tray0 = generar_punto_elipse(a-150, b-60, t_tray)
        cv2.circle(imagen, pt_tray0, radius=1, color=(255, 255, 255), thickness=-1)
        pt_tray = generar_punto_elipse(a, b, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)
        pt_tray2 = generar_punto_elipse(a+30, b+30, t_tray)
        cv2.circle(imagen, pt_tray2, radius=1, color=(255, 255, 255), thickness=-1)
        pt_tray3= generar_punto_elipse(a+70, b+70, t_tray)
        cv2.circle(imagen, pt_tray3, radius=1, color=(255, 255, 255), thickness=-1)
    
    
    cv2.imshow('img', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(1)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()