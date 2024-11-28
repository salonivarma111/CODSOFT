# task 4
# Rock-Paper-Scissors Game
import random
while True:
  user_action = input("Enter a choice (rock, paper, scissor): ")
  possible_actions = ["rock", "paper", "scissor"]
  computer_action = random.choice(possible_actions)
  print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")
  if user_action == computer_action:
    print (f"Both players selected {user_action}. It's a tie!")
  elif user_action == "rock":
    if computer_action == "scissor":
      print("Rock smashes scissor! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_action == "paper":
    if computer_action == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissor cuts paper! you lose.")
  elif user_action == "scissor":
    if computer_action == "paper":
      print("Scissor cuts paper! You win!")
    else:
      print("Rock smashes scissor! You lose.")
  play_again = input("Play again? (yes/no): ")
  if play_again.lower() != "yes":
    break