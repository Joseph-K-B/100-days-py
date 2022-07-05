def welcome():
  greeting = print("Welcome to the console..")
  a = input("Where do you hail from?\n")
  b = input("Name the beast!\n")

  c = a
  a = b
  b = c

  band_name = print("Your band shall be deemed" + " " + a + " " + b)

  return greeting, a, b, band_name

welcome()