import sys
import pprint
from collections import defaultdict

text = input("Type a sentence to see the bar chart: ")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

mapped = defaultdict(list)
for character in text:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
