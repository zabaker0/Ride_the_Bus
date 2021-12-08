"""
Author's Name: Sam Herkert
Author's Contact: Sam.herkert@drake.edu
Date: 12/5/21
Collaborator: Zach Baker
"""

from random import *
from deck import *

#Round 1: Red or Black?
def r1():
    result1 = False
    guess = input('Round 1: \nGuess wether the card will be "red" or "black": ')
    if guess == "red" or guess == "black":
        if guess == Card(self.color):
            print(win)
            result1 = True
        if guess != Card(self.color):
            print(lose)
    else:
        print('Invalid input. You must enter "red" or "black".')


def main():
    print('_____________________Ride The Bus_____________________')
    print('Ride The Bus is a card game consisting of 4 rounds, in which the player makes guesses about face down cards. \n') 
    print('How To Play:\n')
    print('For each of the 4 rounds, if the player guesses correctly, they pass that round and move onto the next round. However, if the player guesses incorrectly they fail and restart at round 1. If the player makes it all the way to round 4 and guesses correctly they win the game! \n')
    print('Round 1: The player must guess wether a flipped card will be "black" or "red".\n')
    print('Round 2: The player must guess wether a flipped card will be "higher" or "lower" than the card flipped in round 1. \n')
    print('Round 3: The player must guess wether a flipped card will be "between" or "outside" the cards from round 1 and round 2. \n')
    print('Round 4: The player must guess the suit of a flipped card ("spade", "heart", "clubs", or "diamond"). \n')
    
#win = "Congrats! You guessed correctly. Move on to the next round!"
#lose = "You guessed wrong. Better luck next time!"

#user_input1 = input('Enter anything to continue. Enter "END" to stop playing: ')
#while user_input1 != 'END' and result4 == False:

#calling round 1 function
    print("Let's start! \n")
    r1()
    
main()
