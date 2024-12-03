import glfw
import math
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import sys

pos_x=0
pos_y=3
pos_z=4
speed=1

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def draw_trunk():
    """Dibuja el tronco del árbol como un cilindro"""
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)  # Marrón para el tronco
    glTranslatef(0.0, 0.0, 0.0)  # Posicionar el tronco
    glRotatef(-90, 1, 0, 0)  # Rota para orientar el cilindro verticalmente
    quadric = gluNewQuadric()
    gluCylinder(quadric, 0.3, 0.3, 2.0, 32, 32)  # Radio y altura del cilindro
    glPopMatrix()

def draw_foliage():
    """Dibuja las hojas del árbol como una esfera"""
    glPushMatrix()
    glColor3f(0.1, 0.8, 0.1)  # Verde para las hojas
    glTranslatef(0.0, 2.0, 0.0)  # Posicionar las hojas encima del tronco
    quadric = gluNewQuadric()
    gluSphere(quadric, 1.0, 32, 32)  # Radio de la esfera
    glPopMatrix()

def draw_ground():
    """Dibuja un plano para representar el suelo"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para el suelo
    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)
    glEnd()

def draw_sphere(radius=1, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)
    glPopMatrix()

def draw_cone(base=0.1, height=0.5, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)  # Orientar el cono hacia adelante
    quadric = gluNewQuadric()
    gluCylinder(quadric, base, 0, height, 32, 32)
    glPopMatrix()

def draw_snowman():

    # Cuerpo
    glColor3f(1, 1, 1)
    draw_sphere(1.0, 0, 2, 0)     # Base
    draw_sphere(0.75, 0, 3.2, 0)  # Cuerpo medio
    draw_sphere(0.5, 0, 4.2, 0)   # Cabeza

    # Ojos
    glColor3f(0, 0, 0)
    draw_sphere(0.05, -0.15, 4.3, 0.5)  # Ojo izquierdo
    draw_sphere(0.05, 0.15, 4.3, 0.5)   # Ojo derecho

    # Nariz (cono)
    glColor3f(1, 0.5, 0)  # Color naranja
    draw_cone(0.05, 0.2, 0, 4.2, 0.5)  # Nariz

def draw_tree():
    """Dibuja un árbol completo"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(pos_x, pos_y, pos_z,  # Posición de la cámara
                0, 2, 0,  # Punto al que mira
                0, 1, 0)  #Vector hacia arriba

    draw_ground()  # Dibuja el suelo
    draw_trunk()   # Dibuja el tronco
    draw_foliage() # Dibuja las hojas
    draw_snowman() # Dibuja el muñeco de nieve

    glfw.swap_buffers(window)
    
def key_callback(window, key, scancode, action, mods):
    """Procesa las entradas de teclado"""
    global pos_x, pos_y, pos_z, speed, theta
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            pos_z -= speed  # Mover hacia arriba
            #pos_z += speed
        elif key == glfw.KEY_DOWN:
            pos_z += speed  # Mover hacia abajo
            #pos_z -= speed
        elif key == glfw.KEY_LEFT:
            pos_x -= speed  # Mover a la izquierda
            #pos_z -= speed
        elif key == glfw.KEY_RIGHT:
            pos_x += speed  # Mover a la derecha
            #pos_z += speed
        elif key == glfw.KEY_SPACE:
            pos_y += speed
        elif key == glfw.KEY_LEFT_CONTROL:
            pos_y -= speed


def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Árbol 3D con Tronco y Hojas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)  # Configurar callback de teclado
    glViewport(0, 0, width, height)
    init()


    # Bucle principal
    while not glfw.window_should_close(window):
        draw_tree()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
