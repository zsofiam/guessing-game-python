import random


def process_game(length_of_list, start_range, end_range):
    list_of_numbers = create_list_of_random_numbers(length_of_list, start_range, end_range)
    play_guessing_game(list_of_numbers, start_range, end_range)


def create_list_of_random_numbers(length_of_list, start_range, end_range):
    list_of_random_numbers = []
    for i in range(length_of_list):
        list_of_random_numbers.append(random.randint(start_range, end_range))
    return list_of_random_numbers


def play_guessing_game(list_of_numbers, start_range, end_range):
    for number in list_of_numbers:
        guess = int(input(f"Enter an integer from {start_range} to {end_range}: "))
        while number != guess:
            if guess < number:
                print("guess is low")
                guess = int(input("Enter an integer from 1 to 99: "))
            elif guess > number:
                print("guess is high")
                guess = int(input("Enter an integer from 1 to 99: "))
            else:
                break
        print("you guessed it!")


if __name__ == "__main__":
    process_game(10, 1, 99)
    process_game(10, 1, 49)