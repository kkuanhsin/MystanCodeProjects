"""
File: babygraphics.py
Name: 官欣
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    # the line width between each year line
    line_width = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)

    # the x coordinate
    x = line_width * year_index + GRAPH_MARGIN_SIZE
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # top and bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # year line and year text
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # a and b let the rank fit in the canvas in same scale
    a = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/(MAX_RANK-1)
    b = 20 - a

    color_ct = -1
    for name in lookup_names:

        # choose color
        color_ct += 1
        color = COLORS[color_ct % len(COLORS)]

        # draw line between each year rank
        for i in range(len(YEARS)-1):

            if i < len(YEARS)-2:
                if str(YEARS[i]) in name_data[name]:
                    rank = int(name_data[name][str(YEARS[i])])
                    text = name + ' ' + str(rank)

                    # if no data
                else:
                    rank = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)/a - b/a
                    text = name + ' ' + '*'

                if str(YEARS[i+1]) in name_data[name]:
                    next_rank = int(name_data[name][str(YEARS[i+1])])

                    # if no data
                else:
                    next_rank = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)/a - b/a

                # draw lines
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), rank*a + b,
                                   get_x_coordinate(CANVAS_WIDTH, i+1), next_rank*a + b, fill=color, width=LINE_WIDTH)

                # draw texts
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, rank*a + b,
                                   anchor=tkinter.SW, text=text, fill=color)

            # last line
            else:
                if str(YEARS[i]) in name_data[name]:
                    rank = int(name_data[name][str(YEARS[i])])
                    text = name + ' ' + str(rank)

                    # if no data
                else:
                    rank = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)/a - b/a
                    text = name + ' ' + '*'

                # last point
                if str(YEARS[i+1]) in name_data[name]:
                    last = int(name_data[name][str(YEARS[i+1])])
                    last_text = name + ' ' + str(last)

                    # if no data
                else:
                    last = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)/a - b/a
                    last_text = name + ' ' + '*'

                # draw lines
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), rank*a + b, get_x_coordinate(CANVAS_WIDTH, i+1),
                                   last*a + b, fill=color, width=LINE_WIDTH)

                # last two text
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, rank * a + b,
                                   anchor=tkinter.SW, text=text, fill=color)
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i+1) + TEXT_DX, last * a + b,
                                   anchor=tkinter.SW, text=last_text, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
