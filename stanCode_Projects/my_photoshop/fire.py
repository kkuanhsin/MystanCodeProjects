"""
File: fire.py
Name:官欣
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: the picture of the original
    :return: mark the fire place and other is gray
    """
    fire = SimpleImage(filename)
    for pixel in fire:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg * HURDLE_FACTOR:
            # mark the place on fire
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # turn other place grey
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg

    return fire


def main():
    """
    This program will find is there big fire in the picture,
    and mark the place to red
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
