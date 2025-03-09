# Display Art
import art
import random
from game_data import data


def format_data(account):
    """Takes the account data and print Format the account data in printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

## use if statement to check if user is correct.
def check_answer(user_guess,a_followers,b_followers):
    """Take the user_guess and the follower counts and returns if they got it correct or not"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Compare B: {format_data(account_b)}.")
    # Ask user for a guess.
    guess=input("Who has more followers? Type 'A' or 'B':").lower()

    # Clear the Screen
    print("\n" * 20)
    print(art.logo)

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # Give user the feedback on their Guess.
    # Score Keeping.
    if is_correct:
        score += 1
        print(f"You're Right! Current Score is {score}")
    else:
        print(f"Sorry,You're Wrong! Final Score is {score}")
        game_should_continue = False

# Make the game repeatable.

# Making account at position B become the next account at position A.