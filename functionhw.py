from random import randint
def roll_dice(num_dice):
  # Takes in number of dice to roll.
  dice_rolls = []
  for y in range(num_dice):
    dice_rolls.append(randint(1, 6))
    dice_rolls.sort()
  # For loop rolls each dice randomly.
  return dice_rolls
  # return allows the list of dice rolls to be printed.
print(roll_dice(10))
# The sets the amount of dice to be rolled.
roll = roll_dice
# Demonstrates high order functions
print(roll(4))
# This will print the result of 4 dice rolls.
