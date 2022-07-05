
number = int(input("Which number do you want to check? "))

def even_or_odd():
    if(number % 2 == 0):
        print("This is an even number.")
    else:
        print("This is an odd number.")

even_or_odd()

# Challenge
# My solution 
year = int(input("Which year do you want to check? "))

def is_leap_year():
    if year % 4 == 0 and year % 100 != 0:
        answer = "Leap year."
    elif year % 100 == 0 and year % 400 == 0:
        answer = 'Leap year.'
    else:
        answer = 'Not leap year.'

    return print(answer)

is_leap_year()

# Instructor Solution 
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year.")


# Challenge 
# My Solution 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

def pizza_price():

    price = 0

    if size.upper() == "S":
        price += 15
        if add_pepperoni.upper() == "Y":
            price += 2
        if extra_cheese.upper() == "Y":
            price += 1
    if size.upper() == "M":
        price += 20
        if add_pepperoni.upper() == "Y":
            price += 3
        if extra_cheese.upper() == "Y":
            price += 1
    if size.upper() == "L":
        price += 25
        if add_pepperoni.upper() == "Y":
            price += 3
        if extra_cheese.upper() == "Y":
            price += 1

    return print(f"Your final bill is: ${price}.")

pizza_price()

# Instructor Solution 

if size == "S":
    price += 15
if size == "M":
    price += 20
if size == "L":
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if add_pepperoni == "Y":
    price += 1

print(f"Your final bill is ${bill}.")




