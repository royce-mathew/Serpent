# OpenGL library to use with OpenGL
import glfw

# Import all OpenGL functions
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


# Window class, creates a window with glfw
def create_shader(vertex_filepath, fragment_filepath):
    with open(vertex_filepath, 'r') as vf:
        vertex_src = vf.readlines()

    with open(fragment_filepath, 'r') as ff:
        fragment_src = ff.readlines()

    # Links the vertex and fragment shaders together
    local_shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                                  compileShader(fragment_src, GL_FRAGMENT_SHADER))

    return local_shader


class Window:
    # Initializes a window
    def __init__(self, width: int, height: int, title: str):
        # Check if glfw can be initialized
        if not glfw.init():
            raise Exception("Was not able to initialize glfw")

        # Create a window and set the window as a child of the class
        # Check https://www.glfw.org/docs/latest/group__window.html#ga5c336fddf2cbb5b92f65f10fb6043344 for docs
        self.window = glfw.create_window(width, height, title, None, None)

        # Check if the window was created
        if not self.window:
            # Terminate glfw since we already initialized it in memory
            glfw.terminate()
            raise Exception("glfw window cannot be created")

        # Set the position to 400 pixels to the right and 200 pixels down
        glfw.set_window_pos(self.window, 400, 200)

        # This function makes the OpenGL context of the specified window current on the calling thread.
        glfw.make_context_current(self.window)

    # Tells the program to let user interact with the window, terminate if the program is closed
    def main_loop(self, shader, triangle):
        # Main loop, while the application is open
        while not glfw.window_should_close(self.window):
            # Makes the window respond to mouse and keyboard inputs
            glfw.poll_events()

            #  sets the bitplane area of the window to values previously selected by glClearColor, glClearDepth, and glClearStencil.
            glClear(GL_COLOR_BUFFER_BIT)

            triangle.draw(shader)

            # Makes the back and front buffers swap
            glfw.swap_buffers(self.window)

        triangle.destroy()
        glDeleteProgram(shader)

        # Terminate glfw because we already initialized it
        glfw.terminate()
