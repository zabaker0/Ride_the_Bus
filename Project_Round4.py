#Author's Name: Zach Baker
#Author's Email: zachary.baker@drake.edu
#Date: 10/26/2021
#Collaborator: Sam Herkert

#Round 4

#this is to show the players hand, ignore if N/A
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
        if in_hand ==  'yes':
        if in_hand == 'no':
            print('You win!')
        else:
            print('You lost!')
    else:
        print('What you entered was not valid...')
    
    
    


