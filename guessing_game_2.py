"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
# GOING FOR EXCEEDS

import random

player = input("What is your name?  ")
high_score = 10


def start_game():
  print("\n\n")
  print("Hello {}! Welcome to the Number Guessing Game!".format(player))
  print("\n")
  print("You will be asked to guess the number I randomly chose in my computer brain.")
  print("\n")
  play_game()

def play_game():
  global high_score
  attempts = 1
  secret = random.randint(1, 10)

  try:
    print("The current high score is {}. Lower is better.".format(high_score))
    guess = int(input("Guess a number between 1 and 10:   "))
    while guess != secret:
      if guess == "":
        raise ValueError("Your guess cannot be blank")
        attempts += 1
        continue
      elif guess == 0:
        raise ValueError("Your guess cannot be 0")
        attempts += 1
        continue
      elif guess > 10:
        print("Your guess cannot be greater than 10.")
        attempts += 1
        guess = int(input("Guess:   "))
        continue
      elif guess > secret:
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
      print("\n\n")
      if attempts < high_score:
        high_score = attempts
      play_again = input("Would you like to play again? yes/no  ")
      if play_again.lower() == "no":
        print("Thank you for playing. Good bye.")
      else:
        play_game()

  except ValueError:
    print("That is an invalid entry. Please input only integers between 1 and 10.")
    attempts += 1
    play_game()

# Kick off the program by calling the start_game function.
start_game()