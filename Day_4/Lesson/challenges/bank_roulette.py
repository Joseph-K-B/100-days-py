import random

def bank_roulette():
  name_string = "Angela, Ben, Jenny, Michael, Chloe"
  names = name_string.split(", ")
  
  idx = random.randint(0, len(names))

  print(f"{names[idx]} is going to buy the meal today!")
  
bank_roulette()