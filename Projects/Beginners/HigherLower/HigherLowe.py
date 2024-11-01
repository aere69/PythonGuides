from art import logo,vs
from game_data import data
import random

def select_celebrity():
    return random.choice(data)

def check_answer(celeb_A, celeb_B, guess):
    if celeb_A["follower_count"] > celeb_B["follower_count"]:
        return "A" == guess
    else:
        return "B" == guess

def game():
    game_over = False

    celebrity1 = {}
    celebrity2 = {}

    score = 0

    celebrity1 = select_celebrity()

    while not game_over:
        # Clear the screen
        print("\n" * 20)
        print(logo)
        
        if score != 0:
            print(f"Correct!!!. Current Score : {score}\n")

        print(f"Compare A: {celebrity1["name"]}, a {celebrity1["description"]}, from {celebrity1["country"]}")
        
        print(vs)
        
        celebrity2 = select_celebrity()    

        while celebrity1 == celebrity2:
            celebrity2 = select_celebrity()    

        print(f"Against B: {celebrity2["name"]}, a {celebrity2["description"]}, from {celebrity2["country"]}")

        answer = input("\nWho has more followers, \'A\' or \'B\'? ").upper()

        if check_answer(celebrity1, celebrity2, answer):
            score += 1
            celebrity1 = celebrity2
        else:
            game_over = True

    # Clear the screen
    print("\n" * 20)
    print(logo)
    print(f"You Lost. Your final Score : {score}\n")

game()