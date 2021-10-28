"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

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
  attempts = 1
  secret = random.randint(1, 10)
  try:
    guess = int(input("Guess a number between 1 and 10:   "))
  except ValueError:
    print("That is an invalid entry. Please input only integers between 1 and 10.")
    play_game()
  else:
    while guess != secret:
      if guess > secret:
        print("The number is lower.")
        guess = int(input("Guess:   "))
        attempts += 1
        continue
      elif guess < secret:
        print("The number is higher.")
        guess = int(input("Guess:   "))
        attempts += 1
        continue
    else:
      print("{} you guessed the correct number in {} tries".format(player, attempts))
      print("Game Over!")
  

# Kick off the program by calling the start_game function.
start_game()