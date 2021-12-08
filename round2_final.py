from random import *

#Round 2, Higher or Lower

def round2():
    
    result2 = False
    
    guess = input('Round 2: \nGuess wether the card will be "higher" or "lower": ')
    
    if guess == "higher" or guess == "lower":
        
        if guess == Card(self.number):
            
            print(win)
            
            result2 = True
            
        if guess != Card(self.number):
            
            print(lose)
    else:
        print('Invalid input. You must enter "higher" or "lower".')
        

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

#calling round 2 function
    print("Let's play round 2! \n")
    round2()
    
main()

'''
def round2():
    
    result2 = False
    
    guess = input('Round 2: \nGuess wether the card will be "higher" or "lower": ')
    
    if guess == "higher" or guess == "lower":
        
        if guess == "higher":
            
            if Card_2(self.value) >= Card_1(self.value):
                
                print(win)
                
                result2 = True
            
            elif Card_2(self.value) <= Card_1(self.value):
            
                print(lose)
               
        elif guess == "lower":
            
            if Card_2(self.value) >= Card_1(self.value):
                
                print(lose)
                
            elif Card_2(self.value) <= Card_1(self.value):
                
                print(win)
                
                result2 = True
                
    else:
        print('Invalid input. You must enter "higher" or "lower".')
'''
