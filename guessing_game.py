# a game where player has to guess 10 random numbers in range 1 to 99 
# and 10 random numbers in range 1 to 49
import math #imports math module
import random #imports random module
a = [] #initializes an empty list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
a.append(random.randint(1, 99)) # adds a random number (1-99) to the list
for i in range(10): # the process is done for every element of the list
    g = int(input("Enter an integer from 1 to 99: ")) # player inputs the guess
    while a[i] != g: # while guess is not the number to be guessed this process repeats
        if g < a[i]: # if guess is lower than number to be guessed
            print("guess is low") # prints "guess is low"
            g = int(input("Enter an integer from 1 to 99: ")) # asks for another guess from the player
        elif g > a[i]: # if guess is higher than number to be guessed
            print("guess is high") # prints "guess is high"
            g = int(input("Enter an integer from 1 to 99: ")) # asks for another guess from the player
        else: # the remaining option is true (guess equals the number to be guessed)
            break # breaks out of the cycle
    print("you guessed it!") # plyaer is notofied that they guessed the number

b = [] #initializes an empty list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
b.append(random.randint(1, 49)) # adds a random number (1-49) to the list
for i in range(10): # the process is done for every element of the list
    g = int(input("Enter an integer from 1 to 49: ")) # player inputs the guess
    while b[i] != g: # while guess is not the number to be guessed this process repeats
        if g < b[i]: # if guess is lower than number to be guessed
            print("guess is low") # prints "guess is low"
            g = int(input("Enter an integer from 1 to 49: ")) # asks for another guess from the player
        elif g > b[i]: # if guess is higher than number to be guessed
            print("guess is high") # prints "guess is high"
            g = int(input("Enter an integer from 1 to 49: ")) # asks for another guess from the player
        else: # the remaining option is true (guess equals the number to be guessed)
            break #breaks out of the cycle
    print("you guessed it!") # plyaer is notofied that they guessed the number
