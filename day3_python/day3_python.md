## Lesson 3: Lists and Loops

### 3.1 Introduction to Lists
Lists are mutable sequences that can hold various data types. Here's an example:

```python
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
```

You can add, remove, or change items in a list:

```python
cats.append('Catherine')  # Adds a new cat to the list
del cats[1]  # Removes 'Snappy' from the list
cats[0] = 'Smores'  # Changes the first name 'Tom' to 'Smores'
```

### 3.2 For Loops
The `for` loop is used to iterate over a sequence (like a list or tuple) and perform an action for each item.

Here's a simple example of a `for` loop iterating over a list:

```python
newList = [45, 'eat me', 90210, "The day has come", -67]

for value in newList:
    print(value)
```

---

## Lesson 4: Conditionals and Loops

### 4.1 While Loops
The `while` loop runs as long as a condition is true. Here’s an example:

```python
a = 0
while a < 10:
    print(a)
    a += 1
```

This loop increments `a` by 1 until `a` is no longer less than 10.

### 4.2 Conditional Statements
Conditional statements allow your code to run only if certain conditions are met:

```python
y = 1
if y == 1:
    print("y equals 1")
```

### 4.3 Boolean Expressions
Boolean expressions evaluate to `True` or `False`:

| Expression | Function                 |
| ---------- | ------------------------ |
| `<`        | Less than                |
| `<=`       | Less than or equal to    |
| `>`        | Greater than             |
| `>=`       | Greater than or equal to |
| `!=`       | Not equal to             |
| `==`       | Equal to                 |

### 4.4 More Complex Conditions
Use `else` and `elif` to handle different conditions:

```python
z = 4
if z > 70:
    print("Something is very wrong")
elif z < 7:
    print("This is normal")
```

### 4.5 Indentation in Python
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

---

## Lesson 5: File Handling

### 5.1 Loading a Text File
To read the contents of a text file, you can do the following:

```python
file = open('example.txt')
content_of_file = file.read()
print(content_of_file)
```

However, the more accepted way to do it is using a context manager:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

This code reads the entire content of `example.txt` and prints it to the console.

### 5.2 Saving a Text File
To write to a text file, use the `open` function in write mode. If the file doesn't exist, it will be created:

```python
with open('example.txt', 'w') as file:
    file.write("Hello, world!")
```

This code creates (or overwrites) `example.txt` with the text "Hello, world!".

### 5.3 File Modes
The `open` function supports several modes, determining how the file is handled:

| Mode | Description                                                                   |
| ---- | ----------------------------------------------------------------------------- |
| 'r'  | Read mode. Opens a file for reading (default).                                |
| 'w'  | Write mode. Opens a file for writing (overwrites existing content).           |
| 'a'  | Append mode. Opens a file for writing (appends to existing content).          |
| 'r+' | Read and write mode. Opens a file for both reading and writing.               |
| 'b'  | Binary mode. Used with other modes (e.g., 'rb', 'wb') to handle binary files. |

## Exercise: DNA to RNA (`transcriber.py`)
The goal of this program is, given a file input of a DNA sequence file, convert the DNA sequence into and RNA sequence, and output it to both the terminal and as a new file.

In local directory, make sure you have `./my_seq.fa`, where the sequence is:
```
>my_seq
ATGAGCAAAAAGAAAAAGGAGTGGA
```

Expected behavior:
```
python transcriber.py

Where is the path to the DNA sequence file? ./my_seq.fa

Here is the RNA sequence:
AUGAGCAAAAAGAAAAAGGAGUGGA

Was saved to output_RNA_seq.fa
```

Note `transcriber.py` handles invalid sequences --> "Apples" should not be transcribed!
## For next class:
- Download Miniconda (if not installed already)
```shell
# Downlaod miniconda installer:
curl -o ./miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Then run the installer:
bash ./miniconda.sh
```
