# Import all OpenGL functions
from OpenGL.GL import *
from modules import window
from modules import triangle

# Only run if the program is run, don't run if this file is imported
if __name__ == "__main__":
    # Create a window with the size 1280x720
    win = window

    # glClearColor specifies the red, green, blue, and alpha values
    #   used by glClear to clear the color buffers. takes in rgb and alpha value
    glClearColor(0, 0.1, 0, 1)
    shader = win.create_shader("shaders/vertex.txt", "shaders/fragment.txt")
    triangle = triangle.Triangle(shader)

    # start the main loop (lets us interact with the window)
    win.main_loop(shader, triangle)
