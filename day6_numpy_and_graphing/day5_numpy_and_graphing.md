#### 0. Setting up a conda environment
##### Step 1: Install Conda
```bash
# Downlaod miniconda installer:
wget -O ./miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Then run the installer:
bash ./miniconda.sh
```
##### Step 2: Create a New Conda Environment
Once Conda is installed, open your terminal and create a new environment. Let's name the environment `intro_to_prog` and install Python 3.9 or your preferred version.

```bash
conda create --name intro_to_prog python=3.12
```

Press `y` when prompted to confirm the installation. This command creates a new isolated environment with Python 3.12.

##### Step 3: Activate the Environment
Activate the newly created environment to start working in it.

```bash
conda activate intro_to_prog
```

To get out, do:

```bash
conda deactivate
```


You'll notice that the environment name (`intro_to_prog`) appears before the command prompt, indicating that the environment is active.

##### Step 4: Install Numpy and Matplotlib
Now, let's install `numpy` and `matplotlib` inside this environment using `pip`.

```bash
pip install numpy matplotlib
```

##### Step 5: Verify Installation
To ensure that the packages are installed correctly, you can open a Python shell and try importing the libraries:

```bash
python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
```

#### 1. Introduction to Numpy Arrays

1.1 **What is an Array?**  
Learn about numpy arrays, which are more efficient than Python lists for numerical operations.
- Create a simple 1D array from a list. 
- Check basic attributes: `dtype` and `shape`.

```python
import numpy as np

# Create a simple array
mylist = [2, 5, 3, 9, 5, 2]
myarray = np.array(mylist)

# Check type and shape
print(type(myarray))  # Output: <class 'numpy.ndarray'>
print(myarray.dtype)  # Output: int64
print(myarray.shape)  # Output: (6,)
```

1.2 **Creating Arrays**  
Learn how to generate commonly used arrays:
- Arrays of zeros and ones.
- Diagonal arrays.
- Arrays with a range of values (`arange`, `linspace`).

```python
# Create arrays
zeros_array = np.zeros((2,3))
ones_array = np.ones((2,3))
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)
```

---

#### 2. Basic Operations on Arrays

2.1 **Element-wise Operations**  
Perform mathematical operations that are automatically applied to each element in the array:
- Addition, subtraction, multiplication, division.

```python
# Adding a constant to all elements
myarray + 3

# Multiplying the entire array
myarray * 2
```

2.2 **Mathematical Functions**  
Use numpy's built-in functions for common mathematical operations like trigonometry, exponentials, and logarithms.

```python
# Trigonometric functions
np.sin(myarray)

# Exponentials
np.exp(myarray)

# Logarithms
np.log10(myarray)
```

2.3 **Logical Operations**  
Perform element-wise logical comparisons that return boolean arrays.

```python
# Logical comparison
myarray > 3
```

2.4 **Array Aggregation**  
Apply basic array aggregation functions, such as `sum`, `mean`, `std`, and learn how to apply these along specific axes.

```python
nd_array = np.random.normal(10, 2, (3,4))
nd_array.sum()  # Total sum
nd_array.mean(axis=0)  # Mean along the first axis (rows)
```

---

#### 3. Plotting with Matplotlib

3.1 **Line Plot**  
Create simple line plots using `matplotlib.pyplot`. Use numpy to generate data for plotting.
- Plot a sine wave and a noisy sine wave.

```python
import matplotlib.pyplot as plt

# Create a time array and a sine wave
time = np.arange(0, 10, 0.1)
sine_wave = np.sin(time)
noisy_wave = sine_wave + np.random.normal(0, 0.2, len(sine_wave))

# Plot the sine wave
plt.plot(time, sine_wave)
plt.plot(time, noisy_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave with Noise')
plt.show()

plt.savefig("sin_wave.png")
```

3.2 **Histogram Plot**  
Create a histogram to visualize the distribution of data.

```python
# Plot a histogram of the noisy sine wave
plt.hist(noisy_wave, bins=10)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Noisy Sine Wave')
plt.show()
```

3.3 **Image Plot (2D Array)**  
Visualize 2D arrays as images using `imshow()`. Create a simple 2D random array for this demonstration.

```python
random_array = np.random.rand(5, 5)

plt.imshow(random_array, cmap='viridis')
plt.colorbar()
plt.title('Random 2D Array')
plt.show()
```

---

## Exercise `DNA_to_one-hot_heatmap.py`
Given an user input DNA sequence:
1) Print the sequence back to the user
2) Print one hot encoded matrix of the user's DNA input
3) Show user heat map, where one axis is DNA base number, another is one hot index, and color is 0 or 1.

<div align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SMJejOb3mUJcpV6bwhjnPw.png" alt="one-hot"/>
</div>

![one-hot](https://github.com/zackmawaldi/intro_to_programing/blob/main/misc/Pasted%20image%2020240903194001.png)