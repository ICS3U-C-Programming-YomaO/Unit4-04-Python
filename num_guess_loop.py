#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program asks the user to guess a number

import random


def main():

    # generate a random number between 0 and 9
    correct_number = random.randint(0, 9)

    # start loop
    while True:
        # ask user to guess a number
        user_num = input("Welcome! Guess a number between 0 and 9:")
        try:
            # set user number to int
            user_guess = int(user_num)

            # if user enter a negative integer
            if user_guess < 0:
                print("Please enter a positive integer.")
            else:
                if user_guess == correct_number:
                    print("You guessed correctly!")
                    # end loop
                    break
                else:
                    print("You guessed incorrectly, Try again.")
        # exception handling
        except ValueError:
            print("Please enter a valid integer.")

        # display ending message
        finally:
            print("Thanks for playing!")


if __name__ == "__main__":

    main()
