import random


def process_game(length_of_list, start_range, end_range):
    list_of_numbers = create_list_of_random_numbers(length_of_list, start_range, end_range)
    play_guessing_game(list_of_numbers, start_range, end_range)


def create_list_of_random_numbers(length_of_list, start_range, end_range):
    list_of_random_numbers = []
    for i in range(length_of_list):
        random_number = get_random_number_within_range(start_range, end_range)
        add_random_number_to_list(list_of_random_numbers, random_number)
    return list_of_random_numbers


def add_random_number_to_list(list_of_random_numbers, random_number):
    list_of_random_numbers.append(random_number)


def get_random_number_within_range(start_range, end_range):
    random_number = random.randint(start_range, end_range)
    return random_number


def play_guessing_game(list_of_numbers, start_range, end_range):
    for number in list_of_numbers:
        initiate_and_process_round(number, start_range, end_range)


def initiate_and_process_round(number, start_range, end_range):
    guess = ask_for_user_input_within_range(start_range, end_range)
    process_guesses(number, guess, start_range, end_range)


def process_guesses(number, guess, start_range, end_range):
    while number != guess:
        guess = handle_incorrect_guess_and_ask_for_new_input(number, guess, start_range, end_range)
    handle_correct_guess()


def handle_incorrect_guess_and_ask_for_new_input(number, guess, start_range, end_range):
    handle_incorrect_guess(number, guess)
    guess = ask_for_user_input_within_range(start_range, end_range)
    return guess


def handle_correct_guess():
    print("you guessed it!")


def handle_incorrect_guess(number, guess):
    if guess < number:
        print("guess is low")
    elif guess > number:
        print("guess is high")


def ask_for_user_input_within_range(start_range, end_range):
    guess = int(input(f"Enter an integer from {start_range} to {end_range}: "))
    return guess


if __name__ == "__main__":
    process_game(1, 1, 99)