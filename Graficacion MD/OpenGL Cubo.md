## El objetivo de esta actividad fue agregar un cubo pequeño sobre le cubo previamente generado con OpenGL

#### Importamos las librerias necesarias
~~~
import glfw
from OpenGL.GL import glClearColor, glEnable, glClear, glLoadIdentity, glTranslatef, glRotatef, glMatrixMode
from OpenGL.GL import glBegin, glColor3f, glVertex3f, glEnd, glFlush, glViewport
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, GL_QUADS, GL_PROJECTION, GL_MODELVIEW
from OpenGL.GLU import gluPerspective
import sys
~~~

## Variables globales
~~~
window = None
angle = 0  # Declaramos angle en el nivel superior
~~~

## Función init
~~~
def init():
    # Configuración inicial de OpenGL
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Color de fondo
    glEnable(GL_DEPTH_TEST)  # Activar prueba de profundidad para 3D

    # Configuración de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)

    # Cambiar a la matriz de modelo para los objetos
    glMatrixMode(GL_MODELVIEW)
~~~

## Función para dibujar el cubo
#### Previamente el código incluía dentro de esta función 6 caras que forman al cubo, cada una con color diferente, en base a esto se agregaron 6 caras mas de color blanco, con dimensiones menores y de tal manera que quedara dibujada encima del cubo inicial
~~~
def draw_cube():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpiar pantalla y buffer de profundidad

    # Configuración de la vista del cubo
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10)  # Alejar el cubo para que sea visible
    glRotatef(angle, 2, -1, -1)   # Rotar el cubo en todos los ejes

    glBegin(GL_QUADS)  # Iniciar el cubo como un conjunto de caras (quads)

    # Cada conjunto de cuatro vértices representa una cara del cubo
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f( 1, 1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f(-1, 1, 1)
    glVertex3f( 1, 1, 1)

    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f( 1,-1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)

    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)

    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glVertex3f( 1,-1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f( 1, 1,-1)

    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1, 1)

    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f( 1, 1,-1)
    glVertex3f( 1, 1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1,-1,-1)
    
    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f(0.5, 2.1, -0.5)
    glVertex3f(-0.5, 2.1, -0.5)
    glVertex3f(-0.5, 2.1, 0.5)
    glVertex3f(0.5, 2.1, 0.5)
    
    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f( 0.5, 0.1, 0.5)
    glVertex3f(-0.5, 0.1, 0.5)
    glVertex3f(-0.5, 0.1, -0.5)
    glVertex3f( 0.5, 0.1, -0.5)

    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f( 0.5, 2.1, 0.5)
    glVertex3f(-0.5, 2.1, 0.5)
    glVertex3f(-0.5,-0.1, 0.5)
    glVertex3f( 0.5,-0.1, 0.5)

    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f( 0.5, 0.1, -0.5)
    glVertex3f(-0.5, 0.1, -0.5)
    glVertex3f(-0.5, 2.1, -0.5)
    glVertex3f( 0.5, 2.1, -0.5)

    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f(-0.5, 2.1, 0.5)
    glVertex3f(-0.5, 2.1, -0.5)
    glVertex3f(-0.5, 0.1, -0.5)
    glVertex3f(-0.5, 0.1, 0.5)

    glColor3f(1.0, 1.0, 1.0)  # 2
    glVertex3f( 0.5, 2.1, -0.5)
    glVertex3f( 0.5, 2.1, 0.5)
    glVertex3f( 0.5, 0.1, 0.5)
    glVertex3f( 0.5, 0.1, -0.5)
    

    glEnd()
    glFlush()

    glfw.swap_buffers(window)  # Intercambiar buffers para animación suave
    angle += 1  # Incrementar el ángulo para rotación
~~~
![OpenGL_cubo](Imagenes/opengl_cubo.png)

## Función main
~~~
def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()

    # Crear ventana de GLFW
    width, height = 500, 500
    window = glfw.create_window(width, height, "Cubo 3D Rotando con GLFW", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    # Configurar el contexto de OpenGL en la ventana
    glfw.make_context_current(window)

    # Configuración de viewport y OpenGL
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_cube()
        glfw.poll_events()

    glfw.terminate()  # Cerrar GLFW al salir

if __name__ == "__main__":
    main()