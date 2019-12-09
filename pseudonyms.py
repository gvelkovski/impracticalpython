"""Generate funny names by randomly combining names from 2 separate lists"""
import sys, random

def main():
    """Choose names at random from 2 tuples of names and print to screen"""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder',
             "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks',
             'Chad', 'Chesterfield', 'Chewy',
             'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat')
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh',
            'Clovenhoof', 'Clutterbuck', 'Cocktoasten')

    while True:
        firstName = random.choice(first)
        lastName = random.choice(last)

        print("\n\n")
        #Trick IDLE by using "fatal error" setting to print name in red.
        print("{}{}".format(firstName, lastName), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

        input("\nPress Enter to exit.")

if __name__=="__main__":
    main()
