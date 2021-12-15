Read me File
Ride_the_Bus

Made by Zach Baker, Sam Herkert, Chris Castro, and Chris Tu

Main - Sam
I made a main menu function where all of the rounds and other functions would be called to run the game. It also included a board printing a short description of the game and how to play.

Round 1 - Sam
I made a function for round 1, using a user input to guess black or red, and if statements to determine if the guess was correct. This also set the result1 flag to true if the guess was correct, so the game would move on to the next round.

Round 2- Chris Tu
	Made a function that asked a user for “higher” or “lower”. It relates to the previous card from round 1, if it was a higher card than last round you could move on to the next, if not you would fail. Used if and elif statements to determine this like, “if Card_2(self.value) >= Card_1(self.value):” Sam helped me with these parts in the coding. 

Round 3 Chris Castro 
Using the previous two cards I created a function that decides wether the card drawn is lower than the lowest value in the held cards, and the same if the card drawn is higher value than the highest value card, this is to determine if the card is outside of the value of the cards.  And to determine if the card is inside I created the function inside, meaning that if the card drawn is < than the highest value and > than the lowest value.

Round 4 - Zach Baker
I had made the preliminary round 4 functions, but they need to be changed in order to fit the rest of the file. The rest of the group assisted with this. In the function the user is supposed to guess the suit of the card being drawn, if it is correct the game is over and the player wins, if it is wrong than the player must start over from the beginning.

Deck - Chris Castro 
For the deck we start by creating a class for the card, this contains 3 obj inside of it, suit, value, and color.
After that we create a class for the deck this establishes the 4 different suits and it also gives the card values for 1 to 13 to create the 52 cards

Graphics - Zach
For the graphics all of the card pngs must be downloaded for the file to work. The pngs on Github must also be downloaded and stored in the same folder as the python file.

Slides Presentation - Chris Tu, Sam and Zach
	Chris- Did slides 4-6, half of 8. Wanted to include the rules of the game to show how it is played for people that might not have played before. Wanted to show how we visualized the coding beforehand in 5 and what kind of things we wanted to put in there. 6 is kind of like 5, but it is like not visualized and just things we put down to do. On slide 8 I put down the deck code on the right. I thought this was important to show because the game is centered around a deck.
	Zach - did parts of slides 7 & 8. Slide 7 was the slide of the functions used in the program and slide 8 as copies of the code we made. I helped find which functions we used for slides 7 and had the idea to include example code as part of the presentation. 
	Sam - did the slide giving the overview of the game, and the slides showing an example game.

Code Edits - Sam
I went through all of the code after we put it together, running debug checks and fixing all of the syntax errors and other logistical issues that I could find. 
