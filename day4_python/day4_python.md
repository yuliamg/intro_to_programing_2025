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
