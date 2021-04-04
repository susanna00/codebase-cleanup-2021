
from random import choice

"""
Assigning "rock", "paper", "scissors" as the valid options to refactor duplicate code.
"""


VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    We are expecting two parameters: 
        choice1 and choice2. They are both strings : one of "rock", "paper", or "scissors".
    """
    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice 


if __name__ == '__main__':
    
    #
    # USER SELECTION
    #
   
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u, c)

    if winner == u:
        print("You won!")
    elif winner == c:
        print("Oh no, the computer won!")
    elif winner == None:
        print("It's a tie!")