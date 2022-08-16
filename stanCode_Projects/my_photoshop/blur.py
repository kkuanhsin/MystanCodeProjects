"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original smile face
    :return: the face that is blurred
    """
    # Todo: create a new blank img that is as big as the original one

    blank = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # Todo: get pixel of new_img at x,y

            img_p = img.get_pixel(x, y)
            blank_p = blank.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:

                # Get pixel at the top-left corner of the image.

                a = img.get_pixel(x, y+1)
                b = img.get_pixel(x+1, y+1)
                c = img.get_pixel(x+1, y)
                new_green = (a.green + b.green + c.green + img_p.green)//4
                new_red = (a.red + b.red + c.red + img_p.red)//4
                new_blue = (a.blue + b.blue + c.blue + img_p.blue)//4
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x == img.width - 1 and y == 0:

                # Get pixel at the top-right corner of the image.

                a = img.get_pixel(x - 1, y)
                b = img.get_pixel(x - 1, y + 1)
                c = img.get_pixel(x, y + 1)
                new_green = (a.green + b.green + c.green + img_p.green) // 4
                new_red = (a.red + b.red + c.red + img_p.red) // 4
                new_blue = (a.blue + b.blue + c.blue + img_p.blue) // 4
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x == 0 and y == img.height - 1:

                # Get pixel at the bottom-left corner of the image

                a = img.get_pixel(x, y - 1)
                b = img.get_pixel(x + 1, y)
                c = img.get_pixel(x + 1, y - 1)
                new_green = (a.green + b.green + c.green + img_p.green) // 4
                new_red = (a.red + b.red + c.red + img_p.red) // 4
                new_blue = (a.blue + b.blue + c.blue + img_p.blue) // 4
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x == img.width - 1 and y == img.height - 1:

                # Get pixel at the bottom-right corner of the image

                a = img.get_pixel(x - 1, y)
                b = img.get_pixel(x - 1, y - 1)
                c = img.get_pixel(x, y - 1)
                new_green = (a.green + b.green + c.green + img_p.green) // 4
                new_red = (a.red + b.red + c.red + img_p.red) // 4
                new_blue = (a.blue + b.blue + c.blue + img_p.blue) // 4
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x != 0 and y == 0 and x != img.width - 1:

                # Get top edge's pixels (without two corners)

                a = img.get_pixel(x - 1, y)
                b = img.get_pixel(x + 1, y)
                c = img.get_pixel(x - 1, y + 1)
                d = img.get_pixel(x + 1, y + 1)
                e = img.get_pixel(x, y + 1)
                new_green = (a.green + b.green + c.green + d.green + e.green + img_p.green) // 6
                new_red = (a.red + b.red + c.red + d.red + e.red + img_p.red) // 6
                new_blue = (a.blue + b.blue + c.blue + d.blue + e.blue + img_p.blue) // 6
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x != 0 and y == img.height - 1 and x != img.width - 1:

                # Get bottom edge's pixels (without two corners)

                a = img.get_pixel(x - 1, y)
                b = img.get_pixel(x + 1, y)
                c = img.get_pixel(x - 1, y - 1)
                d = img.get_pixel(x + 1, y - 1)
                e = img.get_pixel(x, y - 1)
                new_green = (a.green + b.green + c.green + d.green + e.green + img_p.green) // 6
                new_red = (a.red + b.red + c.red + d.red + e.red + img_p.red) // 6
                new_blue = (a.blue + b.blue + c.blue + d.blue + e.blue + img_p.blue) // 6
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x == 0 and y != 0 and y != img.height - 1:

                # Get left edge's pixels (without two corners)

                a = img.get_pixel(x, y + 1)
                b = img.get_pixel(x, y - 1)
                c = img.get_pixel(x + 1, y)
                d = img.get_pixel(x + 1, y - 1)
                e = img.get_pixel(x + 1, y + 1)
                new_green = (a.green + b.green + c.green + d.green + e.green + img_p.green) // 6
                new_red = (a.red + b.red + c.red + d.red + e.red + img_p.red) // 6
                new_blue = (a.blue + b.blue + c.blue + d.blue + e.blue + img_p.blue) // 6
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            elif x == img.width - 1 and y != 0 and y != img.height - 1:

                # Get right edge's pixels (without two corners)

                a = img.get_pixel(x, y + 1)
                b = img.get_pixel(x, y - 1)
                c = img.get_pixel(x - 1, y)
                d = img.get_pixel(x - 1, y - 1)
                e = img.get_pixel(x - 1, y + 1)
                new_green = (a.green + b.green + c.green + d.green + e.green + img_p.green) // 6
                new_red = (a.red + b.red + c.red + d.red + e.red + img_p.red) // 6
                new_blue = (a.blue + b.blue + c.blue + d.blue + e.blue + img_p.blue) // 6
                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue

            else:

                # Inner pixels.

                a = img.get_pixel(x - 1, y)
                b = img.get_pixel(x + 1, y)
                c = img.get_pixel(x - 1, y - 1)
                d = img.get_pixel(x, y - 1)
                e = img.get_pixel(x + 1, y - 1)
                f = img.get_pixel(x - 1, y + 1)
                g = img.get_pixel(x, y + 1)
                h = img.get_pixel(x + 1, y + 1)
                new_green = (a.green+b.green+c.green+d.green+e.green+f.green+g.green+h.green+img_p.green)//9
                new_red = (a.red + b.red + c.red + d.red + e.red + f.red + g.red + h.red + img_p.red)//9
                new_blue = (a.blue + b.blue + c.blue + d.blue + e.blue + f.blue + g.blue + h.blue + img_p.blue)//9

                blank_p.green = new_green
                blank_p.red = new_red
                blank_p.blue = new_blue
    return blank


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
