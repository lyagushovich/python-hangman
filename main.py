import os
import methods

os.system('cls' if os.name == 'nt' else 'clear')

print("hangman v0.1")

letters = methods.get_letters()

errors = 0

bad_letters = []
good_letters = []

while errors < 7:
    os.system('cls' if os.name == 'nt' else 'clear')

    methods.print_status(letters, good_letters, bad_letters, errors)

    print("input next letter:")

    user_input = methods.get_user_input()

    result = methods.check_result(user_input, letters, good_letters, bad_letters)

    if result == -1:
        errors += 1
    elif result == 1:
        break

methods.print_status(letters, good_letters, bad_letters, errors)