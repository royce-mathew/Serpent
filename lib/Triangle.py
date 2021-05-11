# import numpy for creating arrays
import numpy as np
# Import all OpenGL functions
from OpenGL.GL import *


class Triangle:
    def __init__(self, shader):
        # We need to use the shader program which is being passed in at creation so we get the information
        glUseProgram(shader)

        # x, y, z, r, g, b
        self.vertices = (
            -0.5, 0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )

        # The datatype has to be float32, by default its 64 bit which acts a bit weird
        # Also create an array using numpy's function because OpenGL does not accept pythons implementation of tuples.
        self.vertices = np.array(self.vertices, dtype=np.float32)

        # Amount of ends that the triangle has
        self.vertex_count = 3

        # Vertex array object; stores all the information about the triangle, so that we can draw it quickly
        self.vao = glGenVertexArrays(1)

        glBindVertexArray(self.vao)

        # vertex buffer object : stores all the data
        self.vbo = glGenBuffers(1)
        # Bind vbo to GLArrayBuffer, anything that we do the the GLArrayBuffer, we're actually doing it to the vbo
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        # nbytes : number of bytes, when we load in data, we need to tell openGL how many bytes we're loading in
        # Draw in static mode (write once use many times)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Enable location 0 of the shader
        glEnableVertexAttribArray(0)
        # Create a pointer to an attribute within our data
        # Parameters: index (location 0 is position),
        #   size (3 bits),
        #   type (floating data),
        #   normalize (already normalized from 0-1)
        #   stride (from one number, how many numbers do we have to step to get to the next number?) * the amount of bytes in a number
        #   pointer (pointer to the first position) [void pointer, points to a pure memory location with no datatype]
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        # Attribute location 1, which is the color
        # ctypes.c_void_p is 3*4 because we start at index 3 and each number has 4 bytes
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(3 * 4))

    def draw(self, shader):
        # Use the provided shader
        glUseProgram(shader)
        # Bind the vao, recalls all of the data and the attributes which was loaded before in the init function
        glBindVertexArray(self.vao)
        # Draw function, put it in triangles mode, start at index 0, and we have 3 corners for the triangle
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

    # Cleans the data of the GPU
    def destroy(self):
        # glDeleteVertexArrays and glDeleteBuffers takes in 2 parameters,
        # the amount of vertex to delete, and a array containing the vertex arrays
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))
