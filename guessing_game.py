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
  

    



"""Psuedo-code Hints
    
When the program starts, we want to:
------------------------------------
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
  a. If the guess greater than the solution, display to the player "It's lower".
  b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it"
      and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over.

( You can add more features/enhancements if you'd like to. )
"""
# write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()