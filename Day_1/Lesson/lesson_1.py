# Data Types 
from __future__ import division


string_type = "string"
integer_type = 4
float_type = 3.48
boolean_type = True

# Type checking
num_char = len(input("Joseph"))

print(num_char)
print(type(num_char))
# Type conversion 
string_num_char = str(num_char)

print(type(string_num_char)) 
# or 
print(type(string_num_char)) 

# Challenge_0
two_digit_number = input("Type a two digit number: ")
####################################

# My solution
string_number = str(two_digit_number)

a = string_number[0]
b = string_number[1]

c = int(a)
d = int(b)

print(c + d)

two_digit_number = input("Type a two digit number: ")

# Instructor solution 
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digint_numer = second_digit + first_digit

print(two_digint_numer)

# Challenge_1
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# My solution 
a = float(height)
b = float(weight)
c = b / a ** 2

print(int(c))

# Instructor solution
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# Round nums (2(arg) = round to hundreth)
print(round(8 / 3, 2))

# Floor division 
print(8 // 3)

# F string 
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}")

# Challenge_2
# My solution  
age = input("What is your current age?")

def time_left():
    years_left = 90 - int(age)
    months_left = years_left * 12
    weeks_left = int(float(years_left) * 52)
    leap_years = years_left / 4
    days_left = years_left * 365

    f_string = print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
    # f_string = print(months_left)
    return f_string

time_left()

# Instructor solution 
age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

print(message)







