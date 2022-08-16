"""
File: hailstone.py
Name:官欣
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    n: int, the number be entered
    This program will make the number you input to 1 with two formula,
    and will tell you how many steps it takes.
    """
    print('This program computes Hailstone sequences')
    print(' ')
    n = int(input('Enter a number: '))
    step = 0
    while n != 1:
        if n % 2 == 0:   # n is even
            a = n//2
            print(str(n)+'  is even, so I take half:   '+str(a))
            n = a
        else:            # n is odd
            b = 3*n + 1
            print(str(n) + '  is odd, so I make 3n+1:   ' + str(b))
            n = b
        step += 1
    print('It took '+str(step)+' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
