import random
from art import logo

# Define global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type \'easy\' or \'hard':").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(user_guess, correct_answer, turns):
    if user_guess == correct_answer:
        print("You guessed it right. You WIN!")
        return -1
    else:
        if user_guess < correct_answer:
            print("Too low")
        else:
            print("Too High")
        return turns - 1

def game():
    print(logo)
    print("Welcome to the number guessing game.")
    print("I am thinking of a number between 1 and 100")
    number = random.randint(1,100)
    number = 5

    attempts = set_difficulty()

    game_over = False

    while not game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_answer(guess,number,attempts)

        if attempts > 0:
            print("Guess Again.")
        else:
            game_over=True

            if attempts == 0:
                print(f"The number was {number} You LOST!.")

game()