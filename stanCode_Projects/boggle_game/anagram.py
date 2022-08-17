"""
File: anagram.py
Name:官欣
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    User input a word and the program will find all anagram
    """
    print('Welcome to stanCode \"Anagram Generator\" (or ' + EXIT + ' to quit)')

    # when the program runs
    while True:
        s = input('Find anagram for: ')
        start = time.time()

        # input EXIT to end the program
        if s == EXIT:
            break
        print('Searching....')

        # find anagrams
        word_lst, count = find_anagrams(s)

        # print result
        print(f'{count} anagrams: {word_lst}')
        end = time.time()

        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    :param s: the word user input
    :return: a list include the possible word in the dictionary
    """
    dict_lst = []

    # read file
    with open(FILE, 'r') as f:
        # loop over
        for line in f:
            # get the same length word
            if len(line.strip()) == len(s):
                # get the character in the word
                if s[0] in line.strip():
                    if s[1] in line.strip():
                        if s[2] in line.strip():
                            dict_lst.append(line.strip())

    return dict_lst


def find_anagrams(s):
    """
    :param s: the word user input
    :return:a list of all anagram
    """
    # the answer list
    word_lst = []
    # the list to check
    check_lst = read_dictionary(s)
    # helper function
    find_anagrams_helper(s, word_lst, '', [], check_lst)

    return word_lst, len(word_lst)


def find_anagrams_helper(s, word_lst, word, index_lst, check_lst):
    """
    :param s: the word you input
    :param word_lst: the answer list
    :param word: the word we find
    :param index_lst: the word index
    :param check_lst: word of the possible dictionary
    """
    # base case
    if len(word) == len(s):
        if word in check_lst:
            if word not in word_lst:
                word_lst.append(word)
                # print the word we find
                print(f'Found: {word}')
                print('Searching....')

    else:
        for i in range(len(s)):
            if i not in index_lst:
                # choose
                word += s[i]
                index_lst.append(i)
                # check if there is a word start with the current answer
                if has_prefix(word, len(s), check_lst):
                    # explore
                    find_anagrams_helper(s, word_lst, word, index_lst, check_lst)
                # un-choose
                word = word[:len(word)-1]
                index_lst.pop()


def has_prefix(sub_s, word_len, check_lst):
    """
    :param sub_s: the part if the word
    :param word_len: the len of the word you input
    :param check_lst: the list of the dictionary
    :return: Boolean
    """
    # loop over the possible word
    for word in check_lst:
        if len(word) <= word_len:
            if word.startswith(sub_s):
                return True


if __name__ == '__main__':
    main()
