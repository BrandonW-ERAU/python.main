import random
def roll_dice(num_dice):
  dice_rolls = []
  int(num_dice)
  for y in range(num_dice):
    dice_rolls.append(random.randint(1, 7))
    dice_rolls.sort()
  return dice_rolls

print(roll_dice(6))

roll = roll_dice

print(roll(4))





