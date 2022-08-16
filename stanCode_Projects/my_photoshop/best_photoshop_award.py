"""
File: best_photoshop_award.py
Name:官欣
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def main():
    """
    創作理念：最近看的超好看電影，謝謝程式讓我圓夢開戰機飛飛還帶上我家的小狗！阿q飛上天～
    """
    back = SimpleImage('image_contest/back.webp')
    me = SimpleImage('image_contest/S__14532611.jpg')
    back.make_as_big_as(me)
    combined_img = combine(back, me)
    combined_img.show()


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
