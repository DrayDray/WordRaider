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
    #if invalid guess keep requesting new one
    while not is_valid_guess(the_guess):
        print("Your guess is invalid! Please try again with a 5-letter word guess.")
        the_guess = input("What is your alternative guess?")
    print("Thanks! Great Guess!")
    return the_guess.lower()



def check_guess(the_guess, word, progress):
    print("Checking your guess...")
    time.sleep(3)  # Sleep for 3 seconds
    misplaced_letters = []
    incorrect_letters = set()


    # Iterate over each letter in the guess
    for i in range(0, len(the_guess)):
        char_guess = the_guess[i]
        #Iterate over the word's characters
        for j in range(0, len(word)):
            char = word[j]
            #exact match
            if i == j and char_guess == char:
                progress[j] = char
                break
            #misplaced match
            elif i != j and char_guess == char:
                misplaced_letters.append(char_guess)
                break
            #no match
            else:
                incorrect_letters.add(char_guess)

    #remove misplaced letters from incorrect_letters list
    for i in range(0, len(misplaced_letters)):
        incorrect_letters.remove(misplaced_letters[i])

    return misplaced_letters, incorrect_letters, progress

def start_guessing(word):
    progress = [None] * 5
    guesses_left = MAX_GUESSES
    print(f"You will be guessing a 5 letter word.\n"
          f"You have {guesses_left} guesses left!")

    print(f'FOR TESTING ONLY - word is {word}')

    while progress != word and guesses_left > 0:
        the_guess = get_valid_guess()
        misplaced_letters, incorrect_letters, progress = check_guess(the_guess, word, progress)
        print(f"Misplaced letters: {misplaced_letters}")
        print(f"Incorrect letters: {incorrect_letters}")
        print(f"Progress of Guess: {progress}")
        guesses_left = guesses_left-1

    if progress != word:
        print("SORRY you ran out of guesses, GAME OVER.")
    else:
        print(f"AMAZING! You won and correctly guessed the word {word}")




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
