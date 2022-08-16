"""
File: hangman.py
Name:官欣
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a hangman game and you need to guess the random word
    """
    times = N_TURNS
    word = random_word()
    blind = ''
    new_ans = ''
    for i in range(len(word)):
        blind += '-'
        new_ans += '-'
    print('The word looks like ' + blind)
    print('You have ' + str(times) + ' wrong guesses left.')
    while True:
        ans = ''
        guess = str(input('Your guess: '))
        guess_up = guess.upper()
        # let all the alpha is upper
        a = word.find(guess_up)
        if guess_up.isalpha():
            if len(guess_up) == 1:
                if a == -1:     # wrong guess
                    times -= 1
                    print('There is no ' + guess_up + '\'s in the word.')
                    if times != 0:
                        print('The word looks like ' + new_ans)
                        print('You have ' + str(times) + ' wrong guesses left.')
                    else:
                        print('You are completely hung : (')
                        print('The word was ' + word)
                        break
                elif a != -1:  # right guess
                    if new_ans == blind:
                        # boundary condition
                        for i in range(len(word)):
                            ch = word[i]
                            if ch == guess_up:
                                ans += ch
                            else:
                                ans += '-'
                        new_ans = ans
                        print('You are correct!')
                        print('The word looks like ' + ans)
                        print('You have ' + str(times) + ' wrong guesses left.')
                    else:
                        for i in range(len(word)):
                            ch = word[i]
                            ch2 = new_ans[i]
                            if ch == guess_up:
                                ans += ch
                            elif ch2.isalpha():
                                ans += ch2
                            else:
                                ans += '-'
                        new_ans = ans
                        if ans == word:
                            # When you get the right ans
                            print('You win!!!')
                            print('The word was ' + word)
                            break
                        else:
                            print('You are correct!')
                            print('The word looks like ' + ans)
                            print('You have ' + str(times) + ' wrong guesses left.')
            else:
                # while input wrong thing
                print('Illegal format.')
        else:
            # while input wrong thing
            print('Illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
