print("Hello World!")

# new line 
print("Using a backslash an n\ncreates a new line")

# concat 
print("Using a +" + " " + " and space characters" + " " + "concatenates strings")

# nested input w/ print
print("Hello " + input("What is your name?"))
# iteration w/ length 
print(len("Hello " + input("What is your name?")))

# swap variables 
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)