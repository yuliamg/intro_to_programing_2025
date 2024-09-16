### 6.1 Defining Your Own Functions
You can define your own functions using the `def` keyword:

```python
def hello():
    print("hello")
    # return 1234

print(hello())
```

### 6.2 Passing Parameters to Functions
Functions can take parameters, allowing them to perform tasks with different inputs:

```python
def add(a, b):
    results = a+b
    return a + b

result = add(5, 10)
print("The result is:", result)
```

```python
def squared(n):
	n_squared = n*n
	return n_squared
```


DEMO:
```python
def calculator(a, operation, b):
	a = int(a)
	b = int(b)
	
	if operation == '+':
		return a + b
	elif operation == '-':
		return a - b
	elif operation == '*':
		return a * b
	elif operation == '/':
		if b == 0:
			return "Cannot divide by zero!"
		else:
			return a / b
	else:
		return "Invalid operation"

calc_input = '1+1'
calculator(calc_input[0], calc_input[1], calc_input[2])
```

### 7.0 Dictionaries
Dictionaries store key-value pairs, allowing you to map one item to another:

```python
phonebook = {'Andrew': 8806336, 'Emily': 6784346, 'Peter': 7658344}
```

You can access, add, or delete entries using the keys:

```python
print(phonebook['Andrew'])  # Outputs: 8806336
phonebook['Gingerbread Man'] = 1234567  # Adds a new entry
del phonebook['Andrew']  # Removes Andrew's entry
```

DEMO:
```python
def base_counter(sequence):
	base_freq = {'A':0, 'T':0, 'G':0, 'C':0}
	for base in sequence:
		base_freq[base] += 1
	return base_freq

seq = input('Input a sequence to count: ')

print(base_counter( seq ))
```

### Exercise: DNA to Amino Acid Converter (`DNA_to_AA.py`)
#### Task:
Write a Python script, `DNA_to_AA.py`, that converts a DNA sequence to its corresponding Amino Acid sequence by performing the following steps:
1. Take user DNA input
2. Convert a DNA sequence to RNA.
3. Translate RNA to Amino Acids using the below dictionary.
4. Use functions to break down the process.
5. Output the Amino Acid sequence to the terminal.
6. Fold the protein! Use [ESMFold](https://esmatlas.com/resources?action=fold) web version.

RNA to AA dictionary:
```python
genetic_code = {
    'AUG': 'M', 
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}
```

Our `mystery_protein.fa`:
```
>mystery_protein_seq
ATGGACAAGGACGAGGCGTGGAAGTGCGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATATGCGACGCGACGGGGCTGGAGCACCACCACCACCACCAC
```

%% ### 8.0 Classes (Object Oriented Programming)

Classes in Python allow you to group related variables and functions into one entity, making it easier to manage complex programs. Think of a class as a blueprint for creating objects. For example, a `Shape` class could define properties like height and width, and methods (functions) like calculating area and perimeter.

### 8.1 Creating a Class
A class is defined using the `class` keyword:

```python
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)
```

Here, `Shape` is a class with two attributes (`x` and `y`) and two methods (`area` and `perimeter`). The `__init__` method initializes the attributes when an instance of the class is created.

### 8.2 Using a Class
To create an object (an instance of the class) and use its methods:

```python
rectangle = Shape(100, 45)
print(rectangle.area())       # Output: 4500
print(rectangle.perimeter())  # Output: 290
```

Each instance of the class (like `rectangle`) is independent and has its own attributes and methods.

### 8.3 Inheritance
Inheritance allows a new class to inherit the properties and methods of an existing class. This makes it easy to create a new class with added features without rewriting the existing code.

```python
class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)

class DoubleSquare(Square):
    def __init__(self, y):
        super().__init__(2 * y)

    def perimeter(self):
        return 2 * self.x + 3 * self.y
```

Here, `Square` inherits from `Shape`, and `DoubleSquare` inherits from `Square`, adding and modifying methods as needed.

#### Key Terms:
- **Class**: A blueprint for creating objects.
- **Instance**: A specific object created from a class.
- **Attribute**: A variable within a class.
- **Method**: A function within a class.
- **Inheritance**: A way to create a new class using details from an existing class.

 %%