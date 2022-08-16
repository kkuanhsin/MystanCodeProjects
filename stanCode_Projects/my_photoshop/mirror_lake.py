"""
File: mirror_lake.py
Name:官欣
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: the picture want to be mirror
    :return: the picture finished mirror
    """
    img = SimpleImage(filename)
    empty = SimpleImage.blank(img.width, img.height*2)
    # create a new blank img
    for x in range(img.width):
        for y in range(img.height):
            empty_p1 = empty.get_pixel(x, y)
            img_p = img.get_pixel(x, y)
            # original img
            empty_p1.red = img_p.red
            empty_p1.green = img_p.green
            empty_p1.blue = img_p.blue
            # mirror img
            empty_p2 = empty.get_pixel(x, empty.height - 1 - y)
            empty_p2.red = img_p.red
            empty_p2.green = img_p.green
            empty_p2.blue = img_p.blue

    return empty


def main():
    """
    This program will mirror the picture.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
