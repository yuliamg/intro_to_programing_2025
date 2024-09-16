# Running Python scripts is done via `python script_name.py` in the terminal.
# Here, we will demonstrate a basic print statement.

print("Hello, everyone!")
# Output:
'''
Hello, everyone!
'''

# Python handles arithmetic operations:
print(2 + 2)   # Output: 4
print(10 - 5)  # Output: 5
print(4 * 3)   # Output: 12
print(8 / 2)   # Output: 4.0
print(2 ** 3)  # Output: 8



# Comments are ignored by Python, use them to explain your code:
# This is a single-line comment.
"""
This is a multi-line comment.
Great for larger explanations!
"""




# Variables store data for later use:
num = 10
print("The value of num is:", num)  # Output: The value of num is: 10


# You can change variable values:
num = num * 2
print("Now num is:", num)  # Output: Now num is: 20


# Strings hold text data:
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!



# Access specific parts of a string:
text = "Python"
print(text[0])   # Output: 'P'  (First character)
print(text[-1])  # Output: 'n'  (Last character)
print(text[:3])  # Output: 'Pyt'  (First 3 characters)


# String methods:
print(text.upper())  # Output: 'PYTHON'  (Uppercase)
print(text.lower())  # Output: 'python'  (Lowercase)
print(text.replace("Python", "Coding"))  # Output: 'Coding'  (Replace part of the string)



# String formatting:
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)  # Output: Alice is 30 years old.


# Lists hold multiple items:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']



# You can modify lists:
fruits.append("orange")
del fruits[0]
print(fruits)  # Output: ['banana', 'cherry', 'orange']


# Boolean expressions:
x = 10
y = 20
print(x == y)  # Output: False (10 is not equal to 20)
print(x != y)  # Output: True (10 is not equal to 20)


# Loop through a list:
for fruit in fruits:
    print(fruit)
# Output:
'''
apple
banana
cherry
orange
'''


# While loops repeat as long as a condition is true:
counter = 0
while counter < 5:
    print(counter)
    counter += 1
# Output:
'''
0
1
2
3
4
'''


# If-else statements allow decision-making:
temperature = 25
if temperature > 30:
    print("It's hot today.")
elif temperature < 15:
    print("It's cold today.")
else:
    print("The weather is nice.")  # Output: The weather is nice.



# Reading from a file (example.txt should exist in the working directory):
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# Output: (Depends on the content of example.txt)
'''
<content of the file>
'''



# Writing to a file:
with open('output.txt', 'w') as file:
    file.write("This is a new file created by Python!")
# Output: A new file named 'output.txt' will be created with the above content.