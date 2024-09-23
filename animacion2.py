import numpy as np
import cv2

def generar_punto_elipse(a, b, t):
    x = int(a * np.cos(t) + 300)  
    y = int(b * np.sin(t) + 300)
    return (x, y)

img_width, img_height = 700, 700
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

a = 200  
b = 100  
num_puntos = 150

t_vals = np.linspace(0, 2 * np.pi, num_puntos)


for t in t_vals:
    
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    
    # Generar el punto en la elipse
    puntoSol = generar_punto_elipse(1, 1, t)
    puntoMer = generar_punto_elipse(45, 40, t*4.14)
    puntoVen = generar_punto_elipse(65, 60, t*1.62)
    puntoTie = generar_punto_elipse(95, 85, t)
    puntoMar = generar_punto_elipse(125, 110, t*0.53)
    puntoJup = generar_punto_elipse(200, 190, (t+10)/10.8)
    puntoSat = generar_punto_elipse(260, 245, t/29.5)
    puntoUra = generar_punto_elipse(300, 290, (t+300)/84)
    puntoNep = generar_punto_elipse(340, 330, (t+200)/165)
    
    # Dibujar el punto en la elipse
    cv2.circle(imagen, puntoSol, radius=30, color=(0, 255, 239), thickness=-1)
    cv2.circle(imagen, puntoMer, radius=3, color=(0, 0, 230), thickness=-1)
    cv2.circle(imagen, puntoVen, radius=10  , color=(63, 63, 139), thickness=-1)
    cv2.circle(imagen, puntoTie, radius=10, color=(193, 47, 62), thickness=-1)
    cv2.circle(imagen, puntoMar, radius=6, color=(37, 161, 199), thickness=-1)
    cv2.circle(imagen, puntoJup, radius=40, color=(0, 150, 196), thickness=-1)
    cv2.circle(imagen, puntoSat, radius=30, color=(64, 188, 226), thickness=-1)
    cv2.circle(imagen, puntoUra, radius=15, color=(202, 141, 94), thickness=-1)
    cv2.circle(imagen, puntoNep, radius=15, color=(209, 97, 12), thickness=-1)
    
    # Dibujar la trayectoria completa de la elipse (opcional, si quieres ver toda la elipse)
    for t_tray in t_vals:
        pt_trayMer = generar_punto_elipse(45, 40, t_tray)
        cv2.circle(imagen, pt_trayMer, radius=1, color=(255, 255, 255), thickness=-1)
        pt_trayVen = generar_punto_elipse(65, 60, t_tray)
        cv2.circle(imagen, pt_trayVen, radius=1, color=(255, 255, 255), thickness=-1)
        pt_trayTie = generar_punto_elipse(95, 85, t_tray)
        cv2.circle(imagen, pt_trayTie, radius=1, color=(255, 255, 255), thickness=-1)
        pt_trayMar= generar_punto_elipse(125, 110, t_tray)
        cv2.circle(imagen, pt_trayMar, radius=1, color=(255, 255, 255), thickness=-1)
        
        pt_trayCin= generar_punto_elipse(150, 140, t_tray)
        cv2.circle(imagen, pt_trayCin, radius=1, color=(255, 255, 255), thickness=-1)
        
        pt_trayJup= generar_punto_elipse(200, 190, t_tray)
        cv2.circle(imagen, pt_trayJup, radius=1, color=(255, 255, 255), thickness=-1)
        pt_traySat= generar_punto_elipse(260, 245, t_tray)
        cv2.circle(imagen, pt_traySat, radius=1, color=(255, 255, 255), thickness=-1)
        pt_trayUra= generar_punto_elipse(300, 290, t_tray)
        cv2.circle(imagen, pt_trayUra, radius=1, color=(255, 255, 255), thickness=-1)
        pt_trayNep= generar_punto_elipse(340, 330, t_tray)
        cv2.circle(imagen, pt_trayNep, radius=1, color=(255, 255, 255), thickness=-1)
    
    
    cv2.imshow('img', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(5)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()