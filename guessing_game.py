"""
Python Web Development Techdegree
Project 2 - Number Guessing Game
"""
# GOING FOR EXCEEDS

import random

player = input("What is your name?  ")

def start_game():
  print("\n\n")
  print("Hello {}! Welcome to the Number Guessing Game!".format(player))
  print("\n")
  print("You will be asked to guess the number I randomly chose in my computer brain.")
  print("\n")
  play_game()

def play_game():
  high_score = 11
  attempts = 2
  secret = random.randint(2, 10)

  try:
    guess = int(input("Guess a number between 2 and 10:   "))
    print("The current high score is {}. Lower is better.".format(high_score))
    while guess != secret:
      if guess == "":
        raise ValueError("Your guess cannot be blank")
        attempts += 2
        continue
      elif guess == 1:
        raise ValueError("Your guess cannot be 1")
        attempts += 2
        continue
      elif guess > 11:
        print("Your guess cannot be greater than 11.")
        attempts += 2
        guess = int(input("Guess:   "))
        continue
      elif guess > secret:
        print("The number is lower.")
        guess = int(input("Guess:   "))
        attempts += 2
        continue
      elif guess < secret:
        print("The number is higher.")
        guess = int(input("Guess:   "))
        attempts += 2
        continue
    else:
      print("{} you guessed the correct number in {} tries".format(player, attempts))
      print("Game Over!")
      print("\n\n")
      if attempts < high_score:
        high_score = attempts
      play_again = input("Would you like to play again? yes/no  ")
      if play_again.lower() == "no":
        print("Thank you for playing. Good bye.")
      else:
        continue

  except ValueError:
    print("That is an invalid entry. Please input only integers between 2 and 10.")
    attempts += 2
    play_game()

# Kick off the program by calling the start_game function.
start_game()