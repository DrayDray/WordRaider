# This is a sample Python script.
import random

MAX_GUESSES = 5
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi there {name}')  # Press ⌘F8 to toggle the breakpoint.


def load_in_word_bank():
    # Open the file in read mode
    with open('wordbank.txt', 'r') as file:
        # Read all the lines of the file into a list
        lines = file.readlines()
    return lines


def choose_word(lines):
    print("Choosing a random word for this round..")
    return random.choice(lines)


def is_valid_guess(the_guess):
    if the_guess.isalpha() and len(the_guess) == 5:
        return True
    else:
        return False


def get_valid_guess():
    the_guess = input("What is your 5-letter-word guess?")
    #if invalid guess keep requesting new one
    while not is_valid_guess(the_guess):
        print("Your guess is invalid! Please try again with a 5-letter word guess.")
        the_guess = input("What is your alternative guess?")
    print("Thanks! Great Guess!")
    return the_guess.lower()


def start_guessing(word):
    misplaced_letters = []
    incorrect_letters = []
    guesses_left = MAX_GUESSES
    turns_taken = 0
    print(f"You will be guessing a 5 letter word.\n"
          f"You have {guesses_left} guesses left!")

    the_guess = get_valid_guess()


def play_game():
    print("Welcome to Word Raider. Get Ready to begin!\n"
          "3...2...1... Here we go!")

    lines = load_in_word_bank()
    chosen_word = choose_word(lines)

    start_guessing(chosen_word)


if __name__ == '__main__':
    gameName = 'Word Raider'
    play_game()
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
