"""
File: stanCodoshop.py
Name: 官欣
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # formula to calculate distance the pixel and the average point
    color_distance1 = (red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2
    color_distance = math.sqrt(color_distance1)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # red_t, green_t, blue_t = 0, 0, 0    # total
    #
    # # plus all the pixel's red, blue, and green
    # for pixel in pixels:
    #     red_t += pixel.red
    #     green_t += pixel.green
    #     blue_t += pixel.blue
    #
    # # get average
    # red = red_t // len(pixels)
    # green = green_t // len(pixels)
    # blue = blue_t // len(pixels)
    #
    # return [red, green, blue]

    # easy way
    return [
        sum(pixel.red for pixel in pixels),
        sum(pixel.green for pixel in pixels),
        sum(pixel.blue for pixel in pixels)
    ]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    mini = float('inf')
    best = None      # the pixel which is closest to the avg point
    for pixel in pixels:

        # get distance of pixels
        d = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])

        # keep the smallest distance and the pixel which have smallest distance
        if d <= mini:
            mini = d
            best = pixel
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect pixels = []

    result_pixel = result.get_pixel(0, 0)

    for y in range(height):
        for x in range(width):
            # empty pixels list for every differ position
            pixels = []

            # get every image in the same pixel
            for image in images:
                pixel = image.get_pixel(x, y)
                result_pixel = result.get_pixel(x, y)

                # put every same position pixel into a list
                pixels.append(pixel)
            best = get_best_pixel(pixels)

            # put one all best pixels
            result_pixel.red = best.red
            result_pixel.blue = best.blue
            result_pixel.green = best.green

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
