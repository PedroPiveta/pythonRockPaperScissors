import random

# Function to play a single game of Rock, Paper, Scissors
def play_game():
  # Print a welcome message
  print("Welcome to Rock, Paper, Scissors!")

  # Create a list of options
  options = ["rock", "paper", "scissors"]

  # Prompt the player to choose an option
  player_choice = input("Choose one: rock, paper, or scissors: ")

  # Check that the player's input is valid
  while player_choice.lower() not in options:
    player_choice = input("Invalid choice. Please choose rock, paper, or scissors: ")

  # Randomly choose an option for the computer
  computer_choice = random.choice(options)

  # Determine the winner based on the rules of the game
  if player_choice.lower() == computer_choice:
    print(f"It's a tie! You both chose {player_choice}.")
  elif player_choice.lower() == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors.")
  elif player_choice.lower() == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock.")
  elif player_choice.lower() == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats paper.")
  else:
    print(f"You lose! {computer_choice.title()} beats {player_choice}.")

# Play the game
play_game()
