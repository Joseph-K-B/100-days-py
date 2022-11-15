import random

def coin_flip():
  flip = random.randint(0, 1)
  if(flip == 0):
    print("Heads")
  else:
    print("Tails")

coin_flip()