# This is a sample Python script.
import random

MAX_GUESSES = 5
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi there {name}')  # Press ⌘F8 to toggle the breakpoint.


#def chooseRandomWord():


def load_in_word_bank():
    # Open the file in read mode
    with open('wordbank.txt', 'r') as file:
        # Read all the lines of the file into a list
        lines = file.readlines()
    return lines


def choose_word(lines):
    print("Choosing a random word for this round..")
    return random.choice(lines)


def start_guessing():
    misplaced_letters = []
    incorrect_letters = []
    guesses_left = MAX_GUESSES
    turns_taken = 0
    print("You will be guessing a 5 letter word.\n"
          "You have {} guesses left!", guesses_left)

    the_guess = input("What is your guess?")


def play_game():
    print("Welcome to Word Raider. Get Ready to begin!"
          "3...2...1... Here we go!")

    lines = load_in_word_bank()
    chosen_word = choose_word(lines)

    start_guessing()


if __name__ == '__main__':
    gameName = 'Word Raider'
    play_game()
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
