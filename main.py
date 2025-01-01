# Display art
from art import logo , vs
from game_data import data
import random


def formate_data(account):
    """ Format the account data into printable Format. """
    account_name =account["name"]
    account_descr =account["Description"]
    account_country= account["Country"]
    return f"{account_name} , a {account_descr}, from {account_country}"

def check_answer(user_guess , a_followers , b_followers):
    """Take a user's guess and the follower count A and B and returns if they got it right. """
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


print(logo)
score = 0
game_should_conitune=True

while game_should_conitune:
    # Generate a random account from the game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A :{formate_data(account_a)}.")
    print(vs)
    print(f"Compare B :{formate_data(account_b)}.")

    # Ask User for a guess.
    guess = input("Who has more Followers? Type 'A' or 'B' : ").lower()

    # Check if user is correct.
    # -Get follower Count of each account

    a_follower_count = account_a["Follower_count"]
    b_follower_count = account_b["Follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guesses
    # Score Keeping
    if is_correct:
        score += 1
        print(f"You are right , Correct Score {score}")
    else:
        print(f"Sorry, that is wring. Final Score : {score}")
        game_should_conitune=False




# Make the game Repeatable.

# Make account at position B become the next account at position A.

