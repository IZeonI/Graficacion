import glfw
from OpenGL.GL import glClear, glClearColor, glBegin, glEnd, glVertex2f, glColor3f, GL_COLOR_BUFFER_BIT, GL_TRIANGLES, GL_QUADS

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "OpenGL con GLFW", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.0, 0.0, 0.0, 1.0)

    while not glfw.window_should_close(window):
        
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # Rojo
        glVertex2f(-0.3, 0.0)    # Vértice inferior izquierdo
        glColor3f(0.0, 1.0, 0.0)  # Verde
        glVertex2f(1, 1)     # Vértice inferior derecho
        glColor3f(0.0, 0.0, 1.0)  # Azul
        glVertex2f(1, -1)      # Vértice superior
        glEnd()
        
        glBegin(GL_QUADS)
        glVertex2f(-1, 1)
        #glColor3f(1.0, 0.0, 0.0)  # Rojo
        glVertex2f(-1, -1)    # Vértice inferior izquierdo
        #glColor3f(0.0, 1.0, 0.0)  # Verde
        glVertex2f(0.0, -1)     # Vértice inferior derecho
        glColor3f(0.5, 0.8, 1.0)  # Azul
        glVertex2f(0.0, 1)      # Vértice superior
        glEnd()

            # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminar GLFW
glfw.terminate()

if __name__ == "__main__":
    main()