# import modules and other .py files required
from hangman_words import word_list
import string
import random

# set up letters and words
# global variable containing all lowercase letters of the alphabet
az_letters = string.ascii_lowercase
letters_to_choose_from = az_letters
print(letters_to_choose_from, len(letters_to_choose_from))
number_of_fails_left = 8

# functions
def get_word_to_play(words: list):
    # extract a random word from the 'hangman_words.py' list
    word_selection = random.randint(0, len(words) - 1)
    return words[word_selection]


def get_progress_graphic(word_in_play):
    # create a representation of the letters still required via underscores
    print(f'There are {len(word_in_play)} letters in the word\n')
    progress_graphic = '_' * len(word_in_play)
    print(progress_graphic)
    return progress_graphic


def check_guess_accuracy(guess_letter, word_in_play, fails_left):
    """
    Check if guess was accurate - if yes, find all indices in the word where the letter is
                                - if no, leave the list empty
    """
    correct_letter_inds = []
    if guess_letter in word_in_play:
        print(f'Your guess was correct!')
        for i in range(len(word_in_play)):
            if guess_letter == word_in_play[i]:
                correct_letter_inds.append(i)
    return correct_letter_inds


def update_progress_to_user(word_in_play, progress_graphic, correct_letter_inds):
    for index in correct_letter_inds:
        updated_progress = progress_graphic[:index] + word_in_play[index] + progress_graphic[(index+1):]
    print(f'Your progress: \'{updated_progress}\'')
    return updated_progress

def play_again_question():
    # asks the user whether or not to play again, and acts accordingly
    for index in correct_letter_inds:
        updated_progress = progress_graphic[:index] + word_in_play[index] + progress_graphic[(index+1):]
    print(f'Your progress: \'{updated_progress}\'')
    return play_again



"""
End of functions, begin implementation
"""

correct_word = get_word_to_play(word_list)
game_progress_graphic = get_progress_graphic(correct_word)

# while play_again = 'y'
# play_again =
name_check = True
while name_check:
    name_input = input("What is your name?\n")
    # check that the name input string contains only alphabetical characters
    if name_input.isalpha():
        name_check = False
        print(f'Nice to meet you, {name_input}. Game on!')
        break
    print(f"Sorry! \'{name_input}\' is not a valid name! Please try again.")


while number_of_fails_left > 0:
    guess_check = True
    while guess_check:
        guess_input = input("Which letter do you think is in the word?\n").lower()
        # check that the name input string contains only alphabetical characters
        if guess_input.isalpha() and len(guess_input) == 1:
            if guess_input in letters_to_choose_from:
                letters_to_choose_from = letters_to_choose_from.replace(guess_input, '')
                print(f'{len(letters_to_choose_from)} letters left to pick from: {letters_to_choose_from}')
                guess_check = False
                guess_letter_inds = check_guess_accuracy(guess_input, correct_word, number_of_fails_left)
                if len(guess_letter_inds) == 0:
                    number_of_fails_left -= 1
                    print(f'Sorry, you guessed wrong! You have {number_of_fails_left} chances left!')
                    if number_of_fails_left == 0:
                        print(f'Bad luck, you lost!')
                else:
                    game_progress_graphic = update_progress_to_user(correct_word, game_progress_graphic, guess_letter_inds)
                    if '_' not in game_progress_graphic:
                        print(f'Congratulations,{name_input}! You\'ve won!')
                        number_of_fails_left = 0
                        break
                    else:
                        print(f'Great work,{name_input}, keep going! You still have {number_of_fails_left} chances')
            else:
                letters_to_choose_from = letters_to_choose_from.replace(guess_input, '')
                print(letters_to_choose_from, len(letters_to_choose_from))
                print(f"Try again! You've already used \'{guess_input}\' for a previous guess!")
        else:
            print(f"Try again! The input can only be a single letter! \'{guess_input}\' is NOT!")

