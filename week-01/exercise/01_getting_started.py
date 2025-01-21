"""
Exercise 1.1: Getting Started
"""
import random


def guessingGame():
    correct = False
    answer = random.randint(1,3)
    while not correct:
        print("Guess what I ate today for lunch!")
        print("A. Pizza, B: Burger, C: Salad")
        result = str(input()).lower()
        if result == "a" or result == "pizza":
            if answer == 1:
                correct = True
                print("You are right!")
                return
        if result == "b" or result == "burger":
            if answer == 2:
                correct = True
                print("You are right!")
                return
        if result == "c" or result == "salad":
            if answer == 3:
                correct = True
                print("You are right!")
                return
        print("Try again!")



if __name__ == "__main__":
    # 1. Ask a question by printing "Guess what I ate today for lunch!" to the standard output.

    # 2. Provide options A, B, and C. (e.g., A: Pizza, B: Burger, C: Salad) by printing them to the standard output.

    # 3. In a loop, prompt the user to select option A, B, or C.
    # 3.1. If the user input is correct, print "You are right!" to the standard output and break the loop.
    # 3.2. If the user input is incorrect, print "Try again!" to the standard output.

    guessingGame()
    # 4. Play the game with your partners!
    pass