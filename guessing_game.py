import random


def process_game(length_of_list, start_range, end_range):
    list_of_numbers = create_list_of_random_numbers(length_of_list, start_range, end_range)
    play_guessing_game(list_of_numbers, start_range, end_range)


def create_list_of_random_numbers(length_of_list, start_range, end_range):
    list_of_random_numbers = []
    for i in range(length_of_list):
        random_number = get_random_number_within_range(start_range, end_range)
        add_random_number_to_list(list_of_random_numbers, random_number)
    print(list_of_random_numbers)
    return list_of_random_numbers


def add_random_number_to_list(list_of_random_numbers, random_number):
    list_of_random_numbers.append(random_number)


def get_random_number_within_range(start_range, end_range):
    random_number = random.randint(start_range, end_range)
    return random_number


def play_guessing_game(list_of_numbers, start_range, end_range):
    for number in list_of_numbers:
        guess = ask_for_user_input_within_range(start_range, end_range)
        while number != guess:
            if guess < number:
                print("guess is low")
                guess = ask_for_user_input_within_range(start_range, end_range)
            elif guess > number:
                print("guess is high")
                guess = ask_for_user_input_within_range(start_range, end_range)
            else:
                break
        print("you guessed it!")


def ask_for_user_input_within_range(start_range, end_range):
    guess = int(input(f"Enter an integer from {start_range} to {end_range}: "))
    return guess


if __name__ == "__main__":
    process_game(2, 1, 99)
    process_game(2, 1, 49)