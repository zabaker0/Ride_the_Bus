#Author's Name: Zach Baker
#Author's Email: zachary.baker@drake.edu
#Date: 10/26/2021
#Collaborator: Sam Herkert

#Round 4

for p in range(players):
    print('{player_list.name}, its your turn')
    
    print('This is your hand')
    player_list.show_hand()
    
    suit_guess = input('Does the suit match any cards in your hand? (yes or no)')
    
    player_list.draw(deck)
    print('You drew \n')
    player_list.show_hand()
    
#guessing the suit
    if suit_guess in ['yes','no']:
        if in_hand == True and prediction == 'yes'
        if in_hand == False and prediction == 'no':
            print('You are win!')
        else:
            print('You lost, take a drink!')
    else:
        print('What you entered was not valid...')
    
    
    


