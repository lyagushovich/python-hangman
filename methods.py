import sys
import os
from colorama import init
from colorama import Fore
from colorama.ansi import Style

init()

def get_letters():
    word = sys.argv[1]

    if word == None or word == "":
        print(Fore.RED + "input correct word")
        print(Style.RESET_ALL)
        sys.exit()
    
    return list(word)

def get_user_input():
    letter = ""

    while letter == "":
        letter = input()

    return letter

def check_result(user_input, letters, good_letters, bad_letters):
    if user_input in good_letters or user_input in bad_letters:
        return 0
    
    if user_input in letters:
        good_letters.append(user_input)

        if len(set(letters)) == len(good_letters):
            return 1
        else:
            return 0
    else:
        bad_letters.append(user_input)
        return -1

def print_word(letters, good_letters):
    result = ""

    for letter in letters:
        if letter in good_letters:
            result += letter + " "
        else:
            result += "_ "
    
    return result

def print_status(letters, good_letters, bad_letters, errors):
    string_letters = "".join(letters)
    string_bad_letters = ",".join(bad_letters)
    print(Fore.BLUE + f"\nWord:({len(letters)}): " + print_word(letters, good_letters))
    print(f"Errors({errors}): {string_bad_letters}")
    print(Style.RESET_ALL)

    if errors >= 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "you lose")
        print(f"guessed word: {string_letters}")
        print(Style.RESET_ALL)
    else:
        if len(set(letters)) == len(good_letters):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.GREEN + "you win")
            print(f"guessed word: {string_letters}")
            print(Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "you have " + str(7 - errors) + " trys")
            print(Style.RESET_ALL)