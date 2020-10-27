import random
def roll_dice(num_dice):
  dice_rolls = []
  for y in range(num_dice):
    dice_rolls.append(random.randint(1, 6))
    dice_rolls.sort()
  return dice_rolls
print(roll_dice(30))
roll = roll_dice
print(roll(4))
