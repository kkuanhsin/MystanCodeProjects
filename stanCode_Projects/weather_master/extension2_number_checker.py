"""
File: extension2_number_checker.py
Name:官欣
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    n: int, the number be entered
    This will the you weather the number is a perfect,abundant, or deficient number.
    """
    print('Welcome to number checker!')
    while True:
        n = int(input('n: '))
        a = 1
        total = 0
        if n == EXIT:
            print('Have a good one!')
            break
        while n > a:
            if n % a == 0:  # find the factor of n and plus all of them
                total += a
            a += 1
        if total == n:
            print(str(n) + ' is a perfect number')
        elif total > n:
            print(str(n) + ' is an abundant number')
        else:
            print(str(n) + ' is a deficient number')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
