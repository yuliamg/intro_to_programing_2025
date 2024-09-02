## Lesson 1: Introduction to Python Programming

### 1.1 Writing and Running Python Scripts
Python programs are simple text files with a `.py` extension. To run a Python script from your command line or terminal, you can type:

```bash
python script_name.py
```

Let’s start by creating a simple Python program. Write and execute the following code in your Python file:

```python
print('Hello, World')
```

This will print "Hello, World" to the screen. Congratulations, you've just written and run your first Python program!

### 1.2 Basic Math in Python
Python can handle basic arithmetic operations. Try running the following lines of code one by one:

```python
print(1 + 1)
print(20 + 80)
print(6 - 5)
print(2 * 5)
print(5 ** 2)
```

These examples demonstrate addition, subtraction, multiplication, and exponentiation. Notice how Python evaluates each expression and returns the result.

You can also combine text with calculations in print statements:

```python
print('One kilobyte is 2^10 bytes, or', 2 ** 10, 'bytes')
```

### 1.3 Order of Operations
Python follows the standard order of operations (PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction). Try these examples:

```python
print(1 + 2 * 3)
print((1 + 2) * 3)
```

Observe how parentheses affect the calculation.

### 1.4 Comments in Python
Comments are lines of text in your code that Python ignores. They're useful for explaining what your code does:

```python
# This is a comment
'''
This is another comment type, usually meant for longer comments
'''

print("This code will run")  # This comment won't affect the code
```

You can also comment out code if you don’t want it to run:

```python
# print("This won't run")
'''
print("This won't run")
'''
```

---

## Lesson 2: Variables and Strings

### 2.1 Variables
Variables store values that can be used and modified later in your program. Here’s a program that demonstrates variables:

```python
v = 1
print("The value of v is now", v)
v = v + 1
print("v now equals itself plus one, making it worth", v)
v = 51
print("v can store any numerical value, to be used elsewhere.")
print("v times 5 equals", v * 5)
v *= 5
print("Now v equals", v)
```

### 2.2 Strings
Variables can also hold text, known as strings. Here’s an example:

```python
word1 = "Good"
word2 = "morning"
word3 = "to you too!"
sentence = word1 + " " + word2 + " " + word3
print(sentence)
```

#### String Manipulation
You can manipulate strings in various ways:

```python
text = "abcdefghij"
print(text[0])  # Print first character
print(text[4])  # Print the 5th character
print(text[:4])  # Print the first four characters
print(text[4:])  # Print from the 5th character onwards
print(text[4:8])  # Print characters from the 5th to the 8th
print(text[-2])  # Print the second last character
print(text[::2])  # Print every second character
```

#### String Methods
You can perform various operations on strings using methods:

```python
print(sentence.upper())
print(sentence.split(" "))
print(sentence.replace("too", "also"))
```

#### String Formatting
You can also format strings using f-strings:

```python
nrOfCharacters = len(sentence)
lastWord = sentence[-4:-1]
print(f"The sentence has {nrOfCharacters} characters and the last word is: {lastWord}")
```

### 2.3 Tab Completion in VSCode
In modern IDEs like VSCode, you can use tab completion to explore methods available for a variable. Try typing `text.` and see the suggestions.

You can also check a method's documentation by typing:

```python
text.startswith?
```

### 2.4 Taking user input.
Python comes with a number of built-in functions that can be used right away. For example, the `input()` function prompts the user for input:

```python
a = input("Type in something, and it will be repeated on screen: ")
print(a)
```
## Exercise: Greeting and Age Calculator
Given input of name and birth year, greet the user, and show the user their age.
Expected behavior:
```
python greeter.py

What's your name? Zack
What year were you born? 2001

Hello, Zack! You are 23 years old.
```
