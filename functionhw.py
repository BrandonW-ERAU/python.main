from random import randint
import sys
sys.setrecursionlimit(999999)
def roll_dice(num_dice):
  yahtzee = []
  dice_rolls = []
  fails = 0
  fails = fails + 1
  for y in range(num_dice):
    dice_rolls.append(randint(1, 6))
    dice_rolls.sort()
    print("Fail", end=' ')
  if dice_rolls[0] != dice_rolls[4]:
    roll_dice(num_dice)
  elif dice_rolls[0] == dice_rolls[4]:
    print("\nyahtzee!!!")
    yahtzee.append(tuple(dice_rolls))
    print(yahtzee)
  return 2
roll_dice(5)







