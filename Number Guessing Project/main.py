import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess,actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess < actual_answer:
        print("You Selected lower Number!")
        return turns - 1
    elif user_guess > actual_answer:
        print("You Selected Higher Number!")
        return turns - 1
    elif user_guess == actual_answer:
        print("You Win, Keep it up!")

def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game! ")
    print("I'm Thinking of a number between 1 to 100.")
    answer = random.randint(1,100)
    print(f"The answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number:")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You run out of guesses, You Lose")
            return
        elif guess != answer:
            print("Guess Again.")
game()