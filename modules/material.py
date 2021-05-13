# Import pillow for image reading
from PIL import Image

# Import all OpenGL functions
from OpenGL.GL import *

# Material class, let's us set a material for a shape
class Material:
    def __init__(self, filepath):
        # GLGenTextures returns n texture names in textures. There is no guarantee that the names form a contiguous
        # set of integers; however, it is guaranteed that none of the returned names was in use immediately before
        # the call to glGenTextures
        self.texture = glGenTextures(1)
        # Bind GL_TEXTURE_2D to self.texture
        glBindTexture(GL_TEXTURE_2D, self.texture)

        # Typically in texture coordinates its U and V as in the X and Y coordinates but in OpenGL its S and T
        # GL_Repeat basically does, if I put an S coordinate of 1.3,
        # then it just repeats the image and samples 30 percent into the adjascent copy of the image
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # There are two filters, a minifying filter, and a magnifying filter GL_NEAREST is a nearest neighbor
        # function, no interpolation, a very gritty function but doesnt matter because we're making it smaller
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        # Linear interpolation is a bit smoother than GL_Nearest
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # We open the image to extract data
        image = Image.open(filepath)
        # Creates a 32 bit representation of every pixel
        image_data = image.convert("RGBA").tobytes()

        # glTextImage2D the target parameter will be specifed as a two-dimensional texture image
        # GL_TEXTURE_2D takes (target, level, internalformat, width, height, border, format, type, pixels
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        # In computer graphics, mipmaps or pyramids are pre-calculated,
        # optimized sequences of images, each of which is a progressively
        # lower resolution representation of the previous.
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        # Let's say if we had a bunch of textures, different maps and stuff.
        # We call it texture index zero, by default, textures are assigned in the order that they are created
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
