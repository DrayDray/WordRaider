# This is a sample Python script.
import random
import time


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
    # if invalid guess keep requesting new one
    while not is_valid_guess(the_guess):
        print("Your guess is invalid! Please try again with a 5-letter word guess.")
        the_guess = input("What is your alternative guess?")
    print("Thanks for guessing!")
    return the_guess.lower()


def check_guess(the_guess, word, progress, word_hash_set, incorrect_letters):
    print("Checking your guess...")
    misplaced_letters = []

    # Iterate over each letter in the guess
    for i in range(0, len(the_guess)):
        char_guess = the_guess[i]
        char_in_word = word[i]

        # check for match
        if word_hash_set.__contains__(char_guess):
            # check for exact match
            if char_guess == char_in_word:
                # record exact match
                progress[i] = char_guess
            else:
                # match in wrong place
                misplaced_letters.append(char_guess)
        else:
            # no match
            incorrect_letters.add(char_guess)

    return misplaced_letters, incorrect_letters, progress


def start_guessing(word):
    progress = [None] * 5
    guesses_left = MAX_GUESSES
    print(f"You will be guessing a 5 letter word.\n"
          f"You have {guesses_left} guesses left!")

    # we don't care about case for this game
    word = word.lower().strip()
    print(f"FOR TESTING ONLY - THE WORD IS {word}")
    word_hash_set = set(word)
    incorrect_letters = set()
    the_guess = ''

    while the_guess != word and guesses_left > 0:
        the_guess = get_valid_guess()
        misplaced_letters, incorrect_letters, progress = check_guess(the_guess, word, progress, word_hash_set,
                                                                     incorrect_letters)
        if the_guess != word:
            print(f"\nMisplaced letters: {misplaced_letters}")
            print(f"Incorrect letters: {incorrect_letters}")
            print(f"EXACT MATCHES: {progress}")
            guesses_left = guesses_left - 1

    if the_guess == word:
        print(f"\nAMAZING! You won and correctly guessed the word {word} ! "
              f"\n START THE FIREWORKS ! ! !")
    else:
        print("\n SORRY - YOU ARE OUT OF GUESSES. BETTER LUCK NEXT TIME. "
          f"\n THE WORD WAS \"{word.upper()}\".")


def play_game():
    print("Welcome to Word Raider. Get Ready to begin!\n")

    lines = load_in_word_bank()
    chosen_word = choose_word(lines)

    start_guessing(chosen_word)


if __name__ == '__main__':
    gameName = 'Word Raider'
    play_game()
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
