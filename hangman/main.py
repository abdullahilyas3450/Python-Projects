import random
from words import words
import string


def get_valid_word():
    word = random.choice(words)
    while ('-' in word) or (' ' in word):
        word = random.choice(words)

    return word.upper()


def hangman():
    lives = 6
    word = get_valid_word()
    # get the alphabets uesd itn the word we are ging to guess
    alphabets_in_word = set(word)
    alphabets = set(string.ascii_uppercase)  # get all the upper ase alphabets in english
    used_alphabets = set()  # empty set

    while len(alphabets_in_word) > 0 and lives != 0:
        print(f'you have {lives} lives left and The letters you have used are: ', ' '.join(used_alphabets))

        word_list = [letter if letter in used_alphabets else '-' for letter in word]
        print ('  Current word: ', ' '.join(word_list))

        user_alphabet = input("Guess a letter: ").upper()
        if user_alphabet in alphabets - used_alphabets:
            used_alphabets.add(user_alphabet)
            if user_alphabet in alphabets_in_word:
                alphabets_in_word.remove(user_alphabet)
            else:
                lives -= 1
        elif user_alphabet in used_alphabets:
            print('You hane already used this alphabet! Please guess again.')
        else:
            print('Not a alphabet try gain')
    if lives == 0:
        print(f'You have died!!! the word was : {word}')
    else:
        print(f'You Won! You have guessed the word: {word}')

hangman()
