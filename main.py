# Import all OpenGL functions
from OpenGL.GL import *

# Import files from modules
from modules import window
from modules import triangle
from modules import material

# Only run if the program is run, don't run if this file is imported
if __name__ == "__main__":
    # Create a window with the size 1280x720
    win = window.Window(1280, 720, "Serpent")

    # glClearColor specifies the red, green, blue, and alpha values
    #   used by glClear to clear the color buffers. takes in rgb and alpha value
    glClearColor(1, 1, 1, 1)
    shader = window.create_shader("shaders/vertex.txt", "shaders/fragment.txt")

    # Use the shader for this window
    glUseProgram(shader)
    # Passing in glUnform 1 integer, query the location of the sampler within the shader and set it to 0
    # Tell the sampler that it is texture zero, when the material is used it tells it to work with texture index zero
    glUniform1i(glGetUniformLocation(shader, "imageTexture"), 0)

    # Get the wood texture
    wood_texture = material.Material("textures/wood.jpeg")

    # Initialize a triangle with the wood texture
    triangle = triangle.Triangle(shader, wood_texture)

    # start the main loop (lets us interact with the window)
    win.main_loop(shader, triangle)
