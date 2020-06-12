from django.db import models

# Create your models here.

# 001 - Import the random module and create a variable called money that starts with 100.
import random

# Starting money total:
totalMoney001 = 100

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
    print("You have {}".format(totalMoney001))
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
    # Update 'totalMoney001' as a global variable to return new total.
    global totalMoney001
    # First conditional statement allows for a winning argument of 'Heads'. 1 is a match to 'Heads.
    if guess == "Heads" and coinSide == 1:
        # 'totalMoney001' equals the starting money plus the bet * 2. (not sure how betting odds work so I just multiplied the wager by two if the user wins and add it to the totalMoney001 variable)
        totalMoney001 = totalMoney001 + (wager1 * 2)
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney001
        headsWins = "Heads, you won! You now have {}".format(totalMoney001)
        print(headsWins)
        return totalMoney001

    # elif statement allows for a winning argument of 'Tails'. 2 is a match to 'Tails.
    elif guess == "Tails" and coinSide == 2:
        # 'totalMoney001' equals the starting money plus the bet.
        totalMoney001 = totalMoney001 + wager1
        # print out the bet as an integer.
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney001
        tailsWins = "Tails, you won! You now have {}".format(totalMoney001)
        print(tailsWins)
        return totalMoney001

    # else statement prints if you loose. E.g if logical comparison operators do not match.
    else:
        # 'totalMoney001' equals the starting money subtracted by the bet as the user lost.
        totalMoney001 = totalMoney001 - wager1
        # print out the bet as an integer (subtracted).
        yourBet = int(wager1)
        print("\n")
        yourBetString = "Your bet is {}".format(yourBet)
        print(yourBetString)
        # print out string iterpolated with totalMoney001
        lost = "You lost! You now have {}".format(totalMoney001)
        print(lost)
        return totalMoney001

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


# Get values for 'wager2' and 'oddOrEven' variables. If the user decides to play again The 'wager2_value_replay()' function will run instead of the original 'wager2_value()', this is so the new 'newTotalMoney' value at the end of calling main 'cho_han()' function will be used instead of old 'totalMoney001' value.

def wager2_value():
    global wager2
    print("You have {}".format(totalMoney001))
    bet2 = input("Please enter your wager: ")
    wager2 = int(bet2)
    return wager2

def wager2_value_replay():
    global wager2
    print("You have {}".format(totalMoney002))
    bet2 = input("Please enter your wager: ")
    wager2 = int(bet2)
    return wager2

def odd_or_even_value():
    global oddOrEven
    oddOrEven = input("Please enter odd or even: ")
    return oddOrEven

# 003 - Create a function that simulates rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
def cho_han(oddOrEven, wager2, totalMoney001):
    # Create 'totalMoney002' as a global variable to return new total.
    global totalMoney002
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

    # Write a conditional statement that uses logical operators to find out if the left over modulo value in 'sumOfTwoDice' is odd or even and prints if the user has guessed correctly. This in turn adds or subtracts the new 'totalMoney002' value. 
    if sumOfTwoDice == 0 and oddOrEven == "even":
        # Add the 'totalMoney' to the winnings
        totalMoney002 = totalMoney001 + (wager2 * 2)
        print("Even!")
        print("You have won {}! you now have {}".format(name, totalMoney002))
        return totalMoney002

    # Create an elif statement that prints if the 'sumOfTwoDice' is odd.
    elif sumOfTwoDice != 0 and oddOrEven == "odd":
         # Add the 'totalMoney' to the winnings
        totalMoney002 = totalMoney001 + (wager2 * 2)
        print("Odd!")
        print("You have won {}! you now have {}".format(name, totalMoney002))
        return totalMoney002

    # Create an else statement that prints if the user looses.
    else:
        # Subtract the 'wager2 ' value from total money.
        totalMoney002 = totalMoney001 - wager2
        print("Sorry {}, you lost! you now have {}".format(name, totalMoney002))
        return totalMoney002

# Call wager2_value, odd_or_even_value, cho_han functions.
wager2_value()
odd_or_even_value()
cho_han(oddOrEven, wager2, totalMoney001)

# Create a function that asks the user if they would like to play Cho Han again. Use a conditional statemnent to re-call the previously called functions including the 'play_cho_han_again()' itself. If the user decides not to play again the else statement will continue to the next game.
def play_cho_han_again():
    playChoHanAgain = input("Would you like to play again! Y/N: ")
    if playChoHanAgain == "Y":
        # call 'wager2_value_replay' instead of original 'wager2_value()'. This will insure that the 'totalMoney002' value will get paste through the replay and not the original 'totalMoney001' from the previous game.
        wager2_value_replay()
        odd_or_even_value()
        cho_han(oddOrEven, wager2, totalMoney002)
        play_cho_han_again()
    else:
        print("\n")
        print("{}, lets play a game of Highest card wins!".format(name))
        print("\n")

# Call play_cho_han_again()
play_cho_han_again()


# --- Cho-Han Function ---

hi = "high"
lo = "low"

def high_low(bet, hiOrLo, numberOfGames):
    # Create 'totalMoney003' as a global variable to return new total.
    global totalMoney003
    # Create 'cardNumber' variable that contains a list of numbers from 1 to 13
    cardNumber = list(range(1,14))*4
    # Create 'cardType' variable that contains a list of the different suits
    cardType = ['diamonds', 'clubs', 'hearts', 'spades']*13
    # Create a for loop that iterates through a control flow for the amount of games stated in 'numberOfGames' perameter.
    for game in range(numberOfGames):
        # Create a while loop that checks if the user has enough money to bet with and still has gaes to play.
        while totalMoney002 >= bet and game < numberOfGames:
            # Zip() the two card lists together and store in 'cardDeck' variable
            cardDeck = list(zip(cardNumber, cardType))
            # Create an empty list called 'PlayerDraw'
            playerDraw = []
            # use 'random.choice()' to mixed the zipped cardDeck variable and append it to the variable 'playerDraw'
            playerDraw.append(random.choice(cardDeck))






# 004 - Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

# def highest_card(wager3, name, userCard, computerCard):
