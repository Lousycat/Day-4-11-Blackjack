from replit import clear
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def Game():
  User = []
  Computer = []
  Outcome = ""
  EndEarlyCheck = 0
  DrawCheck = False

  print(logo)
  
  print("\nWelcome to Blackjack.")

  #Dishing of Cards
  for i in range (0,2):
    User.append(random.choice(cards)) 
    Computer.append(random.choice(cards))
  print(f"This is the computers first card: {Computer[0]}\n\nThis is your hand:{User}\n")

  #Prelim Check
  CScore = sum(Computer)
  UScore = sum(User)
  if UScore == 21:
    Outcome += "Wow! A blackjack!!! The computer had " + str(Computer) + " You Win! "
    EndEarlyCheck += 1
    
  elif CScore == 21:
    Outcome += "Yikes, the computer got a blackjack " + str(Computer) + " Too bad, try again!"
    EndEarlyCheck += 2
  elif UScore == 21 and CScore == 21:
    Outcome += "Wow! You and the computer both got a blackjack! " + str(Computer) + " Sadly it's a tie. Try again!"
    EndEarlyCheck += 3
  else:
    Draw = input("Do you want to draw another card? Y or N\n").lower()
    if Draw == "y" or Draw == "yes":
      DrawCheck = True
    #Drawing the User's hand before moving on to the computers.
    while DrawCheck == True:
      User.append(random.choice(cards))
      UScore = sum(User) 
      #Ace 1/11
      if UScore == 21:
        Outcome += "Wow! A blackjack!!! The computer had " + str(Computer) + " You Win! "
        EndEarlyCheck += 1
        DrawCheck = False
      elif UScore >21 and User.count(11) >= 1:
        User[User.index(11)] = 1
        print(f"\nThis is your new hand {User}")
      else:
        print(f"\nThis is your new hand {User}")
      Draw = input("\nDo you want to draw another card? Y or N\n").lower()
      if Draw != "yes" or Draw != "y":
        DrawCheck = False
            
    #Computer Logic when to draw/hold + Forced Draw(&reveal time)
    while CScore <=16:
      Computer.append(random.choice(cards))
      CScore = sum(Computer)
      if CScore >21 and Computer.count(11) >= 1:
        Computer[Computer.index(11)] = 1
        CScore = sum(Computer)
    
  #Decision who wins or draws
  CScore = sum(Computer)
  UScore = sum(User)
  if EndEarlyCheck != 0:
    print(Outcome)
  else:
    if CScore == 21:
      print(f"Yikes, the computer got a blackjack " + str(Computer) + " Too bad, try again!")
    elif (CScore > UScore and CScore <=21) or (UScore >21 and CScore <=21) :
      print(f"You lost! Your final hand was {User} with {UScore} points, but the computer had {Computer} at {CScore} points. Try again!\n")
    elif (CScore < UScore and UScore <= 21) or (CScore>21 and UScore> 16):
      print(f"You won! Your final hand was {User} with {UScore} points, and the computer had {Computer} at {CScore} points. Congratulations!\n")
    elif (CScore >21 and UScore > 21) or (CScore>21 and UScore <16):
      print(f"You lost! Your final hand was {User} with {UScore} points, and the computer had {Computer} at {CScore} points. But you busted first! Try again!\n")

    else:
      print(f"You tied! Your final hand was {User} with {UScore} points, but the computer also had {Computer} at {CScore} points. Try Again!\n")

  #Play again
  Start = input("\nDo you want to play another game of BlackJack? Type y or n\n")
  if Start == "y" or Start == "yes":
    clear()
    Game()
  else:
    print("Good Game!")

#Outside the Function
print("If you see an 11 it is representative of the ACE card and will hold a value of 11 as long as your hand size is less than 21.\n\nTake note if your score is less than the computer's or below 16, you WILL lose.")

input("\n\nEnter anything to begin\n")
clear()
Game()



