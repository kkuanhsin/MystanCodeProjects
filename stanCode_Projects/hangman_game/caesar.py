"""
File: caesar.py
Name:官欣
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    param n: The number you input
    param secret: The string you input
    This program will arrangement the ALPHABET with the number you input
    and deciphered the secret you input.
    """
    n = int(input('Secret number: '))
    secret = str(input('What\'s the ciphered string? '))
    secret_up = secret.upper()
    new2 = new(n)
    print('The deciphered string is: ' + (deciphered(new2, secret_up)))


def deciphered(new2, secret):
    """
    Compare the new ALPHABET with the secret you input,
    and put it in the original ALPHABET to get the right ans.
    """
    ans = ''
    for i in range(len(secret)):
        ch = secret[i]
        if ch.isalpha():
            a = new2.find(ch)
            ans += ALPHABET[a]

        else:
            ans += ch

    return ans


def new(num):
    """
    Rearrangement the ALPHABET
    """
    new_alphabet = ''
    new_alphabet += ALPHABET[:len(ALPHABET) - num]
    new_alphabet = ALPHABET[len(ALPHABET) - num:] + new_alphabet
    return new_alphabet


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
