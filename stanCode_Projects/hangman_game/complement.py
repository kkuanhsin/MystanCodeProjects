"""
File: complement.py
Name:官欣
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program will  find the complement DNA of  the DNA you input.
    param dna: The dna sequence you input
    """
    dna = str(input('Please give me a DNA strand and I\'ll find the complement: '))
    print('The complement of ' + dna.upper() + ' is ' + build_complement(dna))


def build_complement(dna):
    """
    It will find the matching of the dna each letter
    """
    ans = ''
    for i in range(len(dna)):
        dna_upper = dna.upper()
        # let all be upper
        ch = dna_upper[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'G':
            ans += 'C'
        elif ch == 'C':
            ans += 'G'

    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
