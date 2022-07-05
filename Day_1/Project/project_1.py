# Tip Calculator 

def Tip_Calculator():
  print("Welcome to the tip calculator")
  bill = (float(input("What was the total bill?"))) + (int(input("How much would you like to tip")) * 0.01)
  split = int(input("How many peope are splitting the bill?"))

  # split_bill = round(bill / split)
  split_bill = bill / split
  final_amount = "{:.2f}".format(split_bill)

  return print(f"Each person should pay {final_amount}")

Tip_Calculator()
  