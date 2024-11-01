import random
from art import logo

print(logo)
print("Welcome to the number guessing game.")
print("I am thinking of a number between 1 and 100")
dificulty = input("Choose a dificulty. Type \'easy\' or \'hard':").lower()
game_over = False

number = random.randint(1,100)

if dificulty == "easy":
    attempts = 10
else:
    attempts = 5

while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        game_over = True
    else:
        if guess < number:
            print("Too low")
        else:
            print("Too High")
        attempts -= 1

        if attempts == 0:
            game_over = True
        else:
            print("Guess again.")

if attempts > 0:
    print("You guessed it right. You WIN!")
else:
    print(f"The number was {number} You LOST!.")