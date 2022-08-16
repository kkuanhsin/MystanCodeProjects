"""
File: rocket.py
Name:官欣
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    It will draw a rocket of the SIZE you input,
    and I disassemble to four steps.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    This is the head of the rocket,the /\\ will increase to the SIZE you input.
    """
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(' ', end='')
        for j in range(i + 1):
            print('/', end='')
        for j in range(i + 1):
            print('\\', end='')

        print('')


def belt():
    """
    This is the belt, it will give you + at the first and end,
    = will be twice of the SIZE in middle.
    """
    print('+', end='')
    for i in range(2 * SIZE):
        print('=', end='')
    print('+')


def upper():
    """
    THis is the upper of the rocket, left and right will have |,
    and middle is . and /\\.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE - 1 - i):
            print('.', end='')
        for j in range(i + 1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE - 1 - i):
            print('.', end='')
        for j in range(1):
            print('|')


def lower():
    """
    THis is the upper of the rocket, left and right will have |,
    and middle is . and /\\.
    It is opposite of upper.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE - i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
