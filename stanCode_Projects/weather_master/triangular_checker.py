"""
File: extension3_triangular_checker.py
Name:官欣
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    tn: int, the number be entered
    This program will tells the number is a triangular number or not
    """
    print('Welcome to the triangular number checker!')
    while True:
        tn = int(input('n: '))
        n = 1
        a = (n * (n + 1)) / 2
        # formula of the triangular number
        if tn == EXIT:
            print('Have a good one!')
            break
        elif tn == 1:
            # Boundary conditions
            print(str(tn) + ' is a triangular number.')
        elif a != tn:
            while tn > n:
                # try until tn-1 == n
                a = (n * (n + 1)) / 2
                if a == tn:
                    print(str(tn) + ' is a triangular number.')
                    break
                else:
                    n += 1
                if tn == n:
                    print(str(tn) + ' is not a triangular number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
