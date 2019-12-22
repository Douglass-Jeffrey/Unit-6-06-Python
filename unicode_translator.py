#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This program takes a word and transforms it into unicode letters


def unicode_converter(word):
    # This takes individual letters and transforms them into unicode characters

    unicode_word = ""

    letters = {
        "a": "61",
        "b": "62",
        "c": "63",
        "d": "64",
        "e": "65",
        "f": "66",
        "g": "67",
        "h": "68",
        "i": "69",
        "j": "6a",
        "k": "6b",
        "l": "6c",
        "m": "6d",
        "n": "6e",
        "o": "6f",
        "p": "70",
        "q": "71",
        "r": "72",
        "s": "73",
        "t": "74",
        "u": "75",
        "v": "76",
        "w": "77",
        "x": "78",
        "y": "79",
        "z": "7a",
    }

    # process
    for letter in word:
        if letter in letters:
            unicode_word = unicode_word + letters[letter] + " "
        else:
            return "This word contains unknown characters. Try again."

    return word + " in the roman alphabet is " + unicode_word + " in unicode"


def main():
    # This takes the user's word and passes it to a function which turns the
    # individual letters to unicode

    # input
    word = input("Type the word that you wish to translate to unicode: ")

    # process
    final_word = unicode_converter(word)

    # output
    print(final_word)


if __name__ == "__main__":
    main()
