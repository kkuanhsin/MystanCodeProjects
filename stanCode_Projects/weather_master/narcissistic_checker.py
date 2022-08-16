"""
File: extension4_narcissistic_checker.py
Name:官欣
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    n: int, the number be entered
    It will tells the number you entered is a narcissistic number or not
    """
    print('Welcome to the narcissistic checker! ')
    while True:
        n = int(input('n: '))
        a = n
        b = 1
        # how many numbers it have
        c = n
        total = 0
        if n == EXIT:
            print('Have a good one!')
            break
        elif n < 10:
            # All number <10 is a narcissistic number
            print(str(n) + ' is a narcissistic number')
        elif n >= 10:
            while n > 10:
                n = n//10     # do floor to the number
                b += 1        # get b
            while a > 10:
                r = a % 10    # find every single number of the number
                a = a//10
                total = r ** b + total   # plus every number with ^b
            total = a**b + total         # last number to plus
            if total == c:   # the number itself
                print(str(total) + ' is a narcissistic number')
            else:
                print(str(c) + ' is not a narcissistic number')



if __name__ == '__main__':
    main()
