from django.db import models

# Create your models here.


# 001 - Import the random module and create a variable called money that starts with 100.
import random

money = 100

# 002 - Create a function that simulates flipping a coin and calling either "Heads" or "Tails".
def coin_flip(guess, bet):
    # 'coinside' generates a side of the coin that wins.
    coinSide = random.randint(1,2)
    
    # First conditional statement allows for a winning argument of 'Heads'. 1 is a match to 'Heads.
    if guess == "Heads" and coinSide == 1:
        # 'totalMoney equals the starting money plus the bet.
        totalMoney = money + bet
        # print out the bet as an integer.
        print(int(bet))
        # print out string iterpolated with totalMoney
        headsWins = "Heads, you won! You now have {}"
        headsWins.format(totalMoney)
        print(headsWins)

    





