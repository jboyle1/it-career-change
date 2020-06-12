from django.db import models

# Create your models here.

# 001 - Import the random module and create a variable called money that starts with 100.
import random

# Starting money total:
totalMoney = 100

# Create a greeting function that only runs once. It will add a global value to the name variable. (couldn't return value without assigning it as a global variable?)
def greeting():
    global name
    name = input("Please Enter a Username: ")
    print("\n")
    print("Hello {}".format(name))
    print("Lets play a game of Heads or tails!")
    print("\n")
    return name


# --- Coin Toss Function ---

# Get value for 'wager1' and 'guess' variables that will be used in the coin flip function 

def wager1_value():
    global wager1
    print("You have {}".format(totalMoney))
    print("\n")
    bet1 = input("Please enter your wager: ")
    wager1 = int(bet1)
    return wager1

def guess_value():
    global guess
    print("\n")
    guess = input("Please enter your guess (Heads or Tails): ")
    return guess

# 002 - Create a function that simulates flipping a coin and calling either "Heads" or "Tails".
def coin_flip(guess, wager1):
    # 'coinside' generates a side of the coin that wins.
    coinSide = random.randint(1,2)
    global totalMoney
    # First conditional statement allows for a winning argument of 'Heads'. 1 is a match to 'Heads.
    if guess == "Heads" and coinSide == 1:
        # 'totalMoney' equals the starting money plus the bet * 2. (not sure how betting odds work so I just multiplied the wager by two if the user wins and add it to the totalMoney variable)
        totalMoney = totalMoney + (wager1 * 2)
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        headsWins = "Heads, you won! You now have {}".format(totalMoney)
        print(headsWins)
        return totalMoney

    # elif statement allows for a winning argument of 'Tails'. 2 is a match to 'Tails.
    elif guess == "Tails" and coinSide == 2:
        # 'totalMoney' equals the starting money plus the bet.
        totalMoney = totalMoney + wager1
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        tailsWins = "Tails, you won! You now have {}".format(totalMoney)
        print(tailsWins)
        return totalMoney

    # else statement prints if you loose. E.g if logical comparison operators do not match.
    else:
        # 'totalMoney' equals the starting money subtracted by the bet as the user lost.
        totalMoney = totalMoney - wager1
        # print out the bet as an integer (subtracted).
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney
        lost = "You lost! You now have {}".format(totalMoney)
        print(lost)
        return totalMoney

# Call greeting, wager1_value, guess_value, and coin_flip functions
greeting()
wager1_value()
guess_value()
coin_flip(guess, wager1)

# Create a function that asks the user if they would like to play coin flip again. Use a conditional statemnent to re-call the previously called functions including the 'play_coin_flip_again()' itself. If the user decides not to play again the else statement will continue to the next game.
def play_coin_flip_again():
    playCoinFlipAgain = input("Would you like to play again! Y/N: ")
    if playCoinFlipAgain == "Y":
        wager1_value()
        guess_value()
        coin_flip(guess, wager1)
        play_coin_flip_again()
    else:
        print("\n")
        print("{}, lets play a game of Cho-Han!".format(name))
        print("\n")

# Call play_coin_flip_again()
play_coin_flip_again()


# --- Cho-Han Function ---


# Get values for 'wager2' and 'oddOrEven' variables. If the user decides to play again The 'wager2_value_replay()' function will run instead of the original 'wager2_value()', this is so the new 'newTotalMoney' value at the end of calling main 'cho_han()' function will be used instead of old 'totalMoney' value.

def wager2_value():
    global wager2
    print("You have {}".format(totalMoney))
    bet2 = input("Please enter your wager: ")
    wager2 = int(bet2)
    return wager2

def wager2_value_replay():
    global wager2
    print("You have {}".format(newTotalMoney))
    bet2 = input("Please enter your wager: ")
    wager2 = int(bet2)
    return wager2

def odd_or_even_value():
    global oddOrEven
    oddOrEven = input("Please enter odd or even: ")
    return oddOrEven

# 003 - Create a function that simulates rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
def cho_han(oddOrEven, wager2, totalMoney):
    global newTotalMoney
    # 'dice1' & 'dice2' each generates a number between 1 & 6.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Print out the values of the dice thrown
    roll = input("Press 'Enter' to roll both dice!")
    print(roll)
    print("\n")
    print("Dice 1 = {}".format(dice1))
    print("Dice 2 = {}".format(dice2))
    print("\n")

    # Get the modulo of the sum of the two values added together
    sumOfTwoDice = (dice1 + dice2) % 2

    # Write a conditional statement that uses logical operators to find out if the left over modulo value in 'sumOfTwoDice' is odd or even and prints if the user has guessed correctly. This in turn adds or subtracts the new 'newTotalMoney' value. 
    if sumOfTwoDice == 0 and oddOrEven == "even":
        # Add the 'totalMoney' to the winnings
        newTotalMoney = totalMoney + (wager2 * 2)
        print("Even!")
        print("You have won {}! you now have {}".format(name, newTotalMoney))
        return newTotalMoney

    # Create an elif statement that prints if the 'sumOfTwoDice' is odd.
    elif sumOfTwoDice != 0 and oddOrEven == "odd":
         # Add the 'totalMoney' to the winnings
        newTotalMoney = totalMoney + (wager2 * 2)
        print("Odd!")
        print("You have won {}! you now have {}".format(name, newTotalMoney))
        return newTotalMoney

    # Create an else statement that prints if the user looses.
    else:
        # Subtract the 'wager2 ' value from total money.
        newTotalMoney = totalMoney - wager2
        print("Sorry {}, you lost! you now have {}".format(name, newTotalMoney))
        return newTotalMoney

# Call wager2_value, odd_or_even_value, cho_han functions.
wager2_value()
odd_or_even_value()
cho_han(oddOrEven, wager2, totalMoney)

# Create a function that asks the user if they would like to play Cho Han again. Use a conditional statemnent to re-call the previously called functions including the 'play_cho_han_again()' itself. If the user decides not to play again the else statement will continue to the next game.
def play_cho_han_again():
    playChoHanAgain = input("Would you like to play again! Y/N: ")
    if playChoHanAgain == "Y":
        # call 'wager2_value_replay' instead of original 'wager2_value()'. This will insure that the 'newTotalMoney' value will get paste through the replay and not the original 'totalMoney' from the previous game.
        wager2_value_replay()
        odd_or_even_value()
        cho_han(oddOrEven, wager2, newTotalMoney)
        play_cho_han_again()
    else:
        print("\n")
        print("{}, lets play a game of Highest card wins!".format(name))
        print("\n")

# Call play_cho_han_again()
play_cho_han_again()


# --- Cho-Han Function ---

# hi = "high"
# lo = "low"

# def high_low(bet, hi_or_lo, number_of_games):







# 004 - Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

# def highest_card(wager3, name, userCard, computerCard):
