"""
Zack Mawaldi 09/12/2024
Function: ask user name and year of birth, greet them and tell them their age

Psuedocode:
name --> take input, while asking "What's your name? "
year --> take input, while asking "What year were you born? "

year = int( year ) 

age --> 2024 - year

display to user "Hello, {Name}! You are {Age} years old."
"""
name = input( "What's your name? " )
year = input( "What year were you born? " )

year = int( year )

age = 2024 - year

displayed_text = "Hello, " + name + "! You are " + str(age) + " years old."

print(displayed_text)

# print("Hello,", name, "!", "You are ", str(age), "years old")

"""
int()
str()
float()
"""
