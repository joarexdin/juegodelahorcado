import random
import os

def run():
    IMAGES = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        / \  |
            |
        =========''']

    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra").upper()

        # found = False
        

if __name__ == "__main__":
    run()
