### 5.5 Defining Your Own Functions
You can define your own functions using the `def` keyword:

```python
def hello():
    print("hello")
    return 1234

print(hello())
```

### 5.6 Passing Parameters to Functions
Functions can take parameters, allowing them to perform tasks with different inputs:

```python
def add(a, b):
    return a + b

result = add(5, 10)
print("The result is:", result)
```

### 6.4 Dictionaries
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


### 7.0 Classes (Object Oriented Programming)

Classes in Python allow you to group related variables and functions into one entity, making it easier to manage complex programs. Think of a class as a blueprint for creating objects. For example, a `Shape` class could define properties like height and width, and methods (functions) like calculating area and perimeter.

### 7.1 Creating a Class
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

### 7.2 Using a Class
To create an object (an instance of the class) and use its methods:

```python
rectangle = Shape(100, 45)
print(rectangle.area())       # Output: 4500
print(rectangle.perimeter())  # Output: 290
```

Each instance of the class (like `rectangle`) is independent and has its own attributes and methods.

### 7.3 Inheritance
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
