What is conda? What are environments? Select conda interpeter for a jup VSCode


## Lesson 1: Very Simple Programs

### 1.1 Running Python from the Command Line
To start, let's create a very simple Python program. Write and execute the following code:

```python
print('Hello, World')
```

This will print "Hello, World" to the screen. Congratulations, you've just written your first Python program!

### 1.2 Basic Math in Python
Python can also handle basic arithmetic. Try running the following lines of code one by one:

```python
1 + 1
20 + 80
6 - 5
2 * 5
5 ** 2
```

These examples demonstrate addition, subtraction, multiplication, and exponentiation. Notice how Python evaluates each expression and returns the result.

You can also combine text with calculations in print statements:

```python
print('one kilobyte is 2^10 bytes, or', 2 ** 10, 'bytes')
```

### 1.3 Order of Operations
Python follows standard order of operations. Try these examples:

```python
1 + 2 * 3
(1 + 2) * 3
```

Observe how parentheses affect the calculation.

### 1.4 Comments in Python
Comments are lines of text in your code that Python ignores. They're useful for explaining what your code does:

```python
# This is a comment
print("This code will run")  # This comment is ignored
```

You can comment out code if you don’t want it to run:

```python
# print("This won't run")
```

### Assignments
1. Write an expression to find out how many seconds are in a 365-day year.
2. The Earth is approximately a sphere with a radius of 6370 km. Calculate its volume in cubic meters.
3. Solve the following expression: \( \frac{1}{2} + \frac{\frac{1}{3}}{\frac{1}{4} + \frac{1}{5}} \).

---

## Lesson 2: Programs in a File, Variables, and Strings

### 2.1 Writing Python Scripts
Python programs are just text files with a `.py` extension. Here's a simple script:

```python
# A simple program.
print("Mary had a little lamb")
print("it's fleece was white as snow;")
print("and everywhere that Mary went", end = " ")
print("her lamb was sure to go.")
```

You can run this script from your command line by typing `python script_name.py`.

### 2.2 Variables
Variables store values. Here's a program that demonstrates variables:

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

### 2.3 Strings
Variables can also hold text, known as strings. Here's an example:

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
print(text[4])  # Single character
print(text[:4])  # First four characters
print(text[4:])  # From character 4 onwards
print(text[4:8])  # Characters from 4 to 8
print(text[-2])  # Second last character
print(text[::2])  # Every second character
```

#### String Methods
Try these operations on strings:

```python
print(sentence.upper())
print(sentence.split(" "))
print(sentence.replace("too", "also"))
```

You can also use string formatting:

```python
nrOfCharacters = len(sentence)
lastWord = sentence[-4:-1]
print(f"The sentence has {nrOfCharacters} characters and the last word is: {lastWord}")
```

### 2.4 Tab Completion
In modern IDEs like VSCode, you can use tab completion to explore methods available for a variable. Try typing `text.` and see the suggestions.

You can also check a method's documentation by typing:

```python
text.startswith?
```

---

## Lesson 3: Loops and Conditional Statements

### 3.1 Introduction to Loops
Loops allow you to repeat code. Here's a simple `while` loop:

```python
a = 0
while a < 10:
    a += 1
    print(a)
```

This loop increments `a` by 1 until `a` is no longer less than 10.

### 3.2 Conditional Statements
Conditional statements run code only if certain conditions are met:

```python
y = 1
if y == 1:
    print("y equals 1")
```

### 3.3 Boolean Expressions
Boolean expressions evaluate to `True` or `False`:

| Expression | Function                 |
| ---------- | ------------------------ |
| `<`        | Less than                |
| `<=`       | Less than or equal to    |
| `>`        | Greater than             |
| `>=`       | Greater than or equal to |
| `!=`       | Not equal to             |
| `==`       | Equal to                 |

### 3.4 More Complex Conditions
Use `else` and `elif` to handle different conditions:

```python
z = 4
if z > 70:
    print("Something is very wrong")
elif z < 7:
    print("This is normal")
```

### 3.5 Indentation in Python
Indentation is critical in Python. Code blocks are defined by their indentation level. Here’s a more complex example:

```python
a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Big number!")
    elif a % 2 != 0:
        print("This is an odd number")
    else:
        print("Small and even number")
    a -= 1
```

### Conclusion
This lesson covered basic loops and conditional statements. Next, you'll learn about functions and more advanced concepts.