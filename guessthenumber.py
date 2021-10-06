import random
from art import logo 

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

print(logo)

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def game():
    print("Welcome to the Number Guessing Name!")
    print("I'm thinking of a number between 1 and 100")

    def set_difficulty():
        level = input ("Choose a difficulty.  Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURN
        else:
            return HARD_LEVEL_TURN

#Choosing a random number between 1 and 100.
    answer = random.randint(1,100)
    turns = set_difficulty()
#Make a function to check answer
    
    def check_answer(guess, answer, turns):
        if guess > answer:
            print("Too high.")
            return turns - 1
        elif guess < answer:
            print("Too low.")
            return turns - 1
        else:
            print (f"You got it! The answer was {answer}")
#Make a function to set difficulty


    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
#Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print ("Guess again.")

game()
