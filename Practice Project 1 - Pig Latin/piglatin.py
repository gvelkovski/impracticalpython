"""Pig Latin"""
import sys

vowels = 'aeiouy'

while True:
    word = input("Type a word and get its Pig latin translation: ")

    if word[0] in vowels:
        pig_Latin = word + 'way'
    else:
        pig_Latin = word[1:] + word[0] + 'ay'
    print()
    print("{}".format(pig_Latin), file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter else n to stop)\n")
    if try_again.lower() == "n":
        sys.exit()
