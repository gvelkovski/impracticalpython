"""Pig Latin"""
import sys

"""Define which characters are vowels"""
VOWELS = 'aeiouy'

while True:
    WORD = input("Type a word and get its Pig latin translation:")

    if WORD[0] in VOWELS:
        PIG_LATIN = WORD + 'way'

    else:
        PIG_LATIN = WORD[1:] + WORD[0] + 'ay'
        print()
        print("{}".format(PIG_LATIN), file=sys.stderr)

        TRY_AGAIN = input("\n\nTry again? (Press Enter else n to stop)\n")
        if TRY_AGAIN.lower() == "n":
            sys.exit()
