"""
File: similarity.py (extension)
Name:官欣
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    param short_sequence: The string you input
    param long_sequence: The string you input
    This program will compare the long and short DNA you input,
    and find the most match part.
    """
    long_sequence = str(input('Please give me a DNA sequence to search: '))
    short_sequence = str(input('What DNA sequence would you like to match? '))
    print('The best match is ' + search(long_sequence, short_sequence))


def search(long, short):
    """
    return max_part: find the most similar part of the long sequence and print.
    """
    a = len(long) - len(short)
    # Times need to test
    biggest = 0
    max_part = ''
    long_up = long.upper()
    short_up = short.upper()

    for i in range(a + 1):
        part = ''
        b = 0
        for j in range(len(short)):
            ch_long = long_up[i + j]
            ch_short = short_up[j]
            part += ch_long
            if ch_short == ch_long:
                b += 1
        if biggest <= b:
            biggest = b
            max_part = part
    return max_part


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
