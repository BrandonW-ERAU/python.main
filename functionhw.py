import random
def roll_dice(num_dice):
  int(num_dice)
  for y in range(num_dice):
    dice = random.randint(1, 7)
    print(dice)

roll_dice(8)



