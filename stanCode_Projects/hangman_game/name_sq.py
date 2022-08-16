"""
File: name_sq.py (extension)
Name: 官欣
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program prints a name in a square pattern.
    param name: The string you input
    """
    print('This program prints a name in a square pattern')
    name = str(input('Name: '))
    for i in range(len(name) - 1):
        chi = name[i]
        a = len(name) - 1 - i
        ch = name[a]
        for j in range(len(name)):
            chj = name[j]
            if i == 0:
                # when i = 0 ,j from 0 to last
                if j < len(name) - 1:
                    print(chj, end='')
                else:
                    print(chj)
            elif j == 0:
                # when at the left
                print(chi, end='')
            elif j != len(name) - 1:
                # when in the middle
                print(' ', end='')
            elif j == len(name) - 1:
                # when at the right
                print(ch)
    last = ''
    for i in range(len(name)):
        last = name[i] + last
    print(last)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
