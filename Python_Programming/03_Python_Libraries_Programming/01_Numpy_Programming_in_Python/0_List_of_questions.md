# Practical NumPy Questions (With Clean Formatting)

---

## 1.

Create a NumPy array with values `[10, 20, 30, 40, 50]`.
Print the array and its data type.

---

## 2.

Create two NumPy arrays `[1,2,3]` and `[4,5,6]`.
Perform element-wise addition and print the result.

---

## 3.

Create a NumPy array from **1 to 10** using a NumPy function (not a Python list).
Print the array.

---

## 4.

Multiply all elements of a NumPy array `[2,4,6,8]` by 5 and print the output.

---

## 5.

Create a 2D NumPy array:

```
[[1,2,3],
 [4,5,6]]
```

Print:

* The array
* Its shape

---

## 6.

Create a NumPy array `[5,10,15,20]` and calculate:

* Sum
* Mean

---

## 7.

Create a NumPy array `[1,2,3,4]` and add 10 to each element using broadcasting.

---

## 8.

Create a NumPy array of size 5 with all elements as 0, then change it to all 1s.

---

## 9.

Create a NumPy array `[1,2,3,4,5]` and compute:

* Square of each element
* Square root of each element

---

## 10.

Create two arrays:

```
a = [1,2,3]
b = [10,20,30]
```

Perform element-wise multiplication and print the result.

---

## 11.

Create the following arrays:

* A scalar (0D) with value `100`
* A 1D array `[1, 2, 3]`
* A 2D array `[[1,2],[3,4]]`

Print the **number of dimensions (`ndim`)** for each.

---

## 12.

Create a 2D NumPy array:

```
[[10, 20, 30],
 [40, 50, 60]]
```

Print:

* Shape
* Total size

Verify:

```
size = rows × columns
```

---

## 13.

Create an array using `np.arange()` from **5 to 15**:

* Print the array
* Print its dtype
* Convert it to float and print again

---

## 14.

Create a NumPy array using `np.linspace()` from **0 to 5** with **6 elements**:

* Print the array
* Print its shape and ndim

---

## 15.

Create a **3×3 matrix of zeros**

Then:

* Convert it into a matrix of ones
* Print both arrays

---

## 16.

Generate a **2×2 random array**:

* Print the array
* Print dtype, itemsize, and nbytes

---

## 17.

Create an array:

```
[1, 2, 3, 4]
```

Print:

* itemsize
* nbytes

Verify:

```
nbytes = itemsize × number of elements
```

---

## 18.

Create an array:

```
[1, 2.5, 3]
```

* Print the array
* Print dtype
* Explain dtype choice

---

## 19.

Create a 3D array:

```
[
 [[1,2],[3,4]],
 [[5,6],[7,8]]
]
```

Print:

* ndim
* shape
* size

---

## 20.

Create any 2D NumPy array and perform complete inspection:

Print:

* Array
* ndim
* shape
* size
* dtype
* itemsize
* nbytes
* flags

---

## 21.

Create an array using `np.empty()` of size 5:

* Print the array
* Observe values
* Assign `[1,2,3,4,5]` manually
* Print again

---

## 22.

Create a **2×3 array filled with 7** using `np.full()`:

* Print the array
* Verify all values are identical

---

## 23.

Use `np.logspace()` to generate 4 values from **10¹ to 10⁴**:

* Print the array
* Explain value generation

---

## 24.

Create:

* A **4×4 identity matrix** using `np.identity()`
* A **3×5 matrix** using `np.eye()`

Print both and compare.

---

## 25.

Generate random arrays:

* `np.random.rand(2,2)`
* `np.random.randint(1,10, (2,2))`

Set a random seed and regenerate one array.
Print all outputs.

---

## 26.

Create array:

```
[1, 2, 3, 4]
```

* Print dtype
* Explain dtype

---

## 27.

Create two arrays:

* `dtype=np.int8`
* `dtype=np.int64`

Print:

* itemsize
* Compare memory

---

## 28.

Create array:

```
[10, 20, 30]
```

* Use `dtype=float32`
* Print dtype and itemsize

---

## 29.

Create:

```
[1.5, 2.7, 3.9]
```

* Convert to integer
* Observe decimal behavior

---

## 30.

Create:

```
[0, 1, 2, 0, 5]
```

* Convert to boolean
* Explain conversion

---

## 31.

Create:

```
[10, 20, 30, 40]
```

* Apply condition `> 25`
* Print mask
* Print filtered result

---

## 32.

Create complex array:

```
[1+2j, 3+4j, 5+6j]
```

Print:

* dtype
* Real part
* Imaginary part

---

## 33.

Create:

```
[1, "hello", 3.5]
```

* Force `dtype=object`
* Try `+1` operation
* Observe behavior

---

## 34.

Convert array step-by-step:

```
[1, 2, 3, 4]
```

* To float
* To string
* Print dtype after each

---

## 35.

Create arrays:

* `float32`
* `float64`

Compare:

* dtype
* itemsize
* memory usage

---

## 36.

Array:

```
[10, 20, 30, 40, 50]
```

Access:

* First element
* Third element
* Last element

---

## 37.

Using same array:

* Last element (negative index)
* Second last
* Compare with positive indexing

---

## 38.

Array:

```
[5, 10, 15, 20]
```

* Modify second element to 100

---

## 39.

Array:

```
[2, 4, 6, 8, 10]
```

* Access two elements
* Perform operation

---

## 40.

2D Array:

```
[[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]]
```

Access:

* (0,1)
* (2,2)
* (1,0)

---

## 41.

Using same array:

* Second row
* First column

---

## 42.

3D Array:

```
[
 [[1,2,3],[4,5,6]],
 [[7,8,9],[10,11,12]]
]
```

Access:

* [0,1,2]
* [1,0,1]

---

## 43.

2D Array:

```
[[1,2,3],
 [4,5,6]]
```

Access:

* Last element
* First row, last column

---

## 44.

Array:

```
[10, 20, 30, 40, 50]
```

Select indices `[0,2,4]` using:

* Manual indexing
* Advanced indexing

---

## 45.

2D Array:

```
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

Use advanced indexing to extract:

* (0,1) and (2,2)

---

---

## 46.

Create a 1D NumPy array:

```
[10, 20, 30, 40, 50, 60]
```

Extract:

* Elements from index **1 to 4**
* First **3 elements**
* Elements from index **3 to end**

---

## 47.

Create a 2D array:

```
[[10,20,30],
 [40,50,60],
 [70,80,90]]
```

Extract:

* First **two rows**
* Rows from index **1 to end**

---

## 48.

Using the same 2D array:

Extract:

* Second column
* First **two columns**
* Last column using **negative indexing**

---

## 49.

Create a 1D array:

```
[10, 20, 30, 40, 50, 60]
```

Extract using slicing:

* Every **second element**
* Elements from index **1 to 5** with step **2**
* Reverse the array using slicing

---

## 50.

Create a NumPy array:

```
[1, 2, 3, 4, 5]
```

Perform:

* Create a slice from index **1 to 4**
* Modify the **first element of the slice**
* Print original array and observe changes

Then:

* Repeat using `.copy()`
* Verify that original array **does NOT change**

---

---

## 51.

Create a NumPy array:

```
[10, 20, 30, 40, 50]
```

* Create a boolean array using condition `> 25`
* Print:

  * Original array
  * Boolean mask

---

## 52.

Using the same array:

```
[10, 20, 30, 40, 50]
```

* Filter and print elements **greater than 25** using boolean indexing

---

## 53.

Create a NumPy array:

```
[1, 2, 3, 4, 5, 6]
```

* Extract all **even numbers** using a condition
* Print the result

---

## 54.

Create a NumPy array:

```
[10, 55, 32, 70, 90, 25]
```

Extract elements:

* Greater than **50**
* Less than or equal to **30**

---

## 55.

Create a 2D NumPy array:

```
[[10,20,30],
 [40,50,60],
 [70,80,90]]
```

* Extract all elements **greater than 50**
* Print the result

---

## 56.

Create a NumPy array:

```
[10, 20, 30, 40, 50, 60]
```

* Extract values:

  * Greater than **20** AND less than **50**
* Use bitwise operator `&`

---

## 57.

Using the same array:

* Extract values:

  * Less than **20** OR greater than **50**
* Use bitwise operator `|`

---

## 58.

Using the same array:

* Extract values that are **NOT greater than 30**
* Use operator `~`

---

## 59.

Create a NumPy array:

```
[10, 20, 30, 40, 50]
```

Use NumPy logical functions:

* `np.logical_and()`
* `np.logical_or()`
* `np.logical_not()`

Apply conditions and print results

---

## 60.

Create a NumPy array:

```
[-3, 5, -1, 7, -8]
```

* Replace all **negative values with 0** using boolean indexing
* Print the updated array

---


## 61.
Create a 1D NumPy array:
[10, 20, 30, 40]

- Iterate through the array using a loop  
- Print each element one by one  

---

## 62.
Create a 2D NumPy array:
[[10,20,30],
 [40,50,60],
 [70,80,90]]

- Iterate through the array row-wise  
- Then use a nested loop to print each element individually  

---

## 63.
Using the same 2D array:
- Iterate **column-wise** using transpose (`.T`)  
- Print each column  

---

## 64.
Create a 2D array:
[[1,2],
 [3,4]]

- Use `np.nditer()` to iterate through all elements  
- Modify each element by multiplying it by 2 using `op_flags=['readwrite']`  
- Print the updated array  

---

## 65.
Create a 2D array:
[[10,20],
 [30,40]]

- Use `np.ndenumerate()` to:
  - Print index and value for each element  

Then:
- Compare this with normal iteration and explain when `ndenumerate()` is useful  

---



## 66.
Create a NumPy array:
[10, 20, 30]

- Add a scalar value `5` to the array  
- Perform multiplication with scalar `2`  
- Print both results  

---

## 67.
Create two arrays:
A = [[1,2,3],
     [4,5,6]]

B = [10,20,30]

- Perform element-wise addition using broadcasting  
- Print the result  
- Explain how NumPy expands array `B`  

---

## 68.
Create two arrays:
A = [[1,2,3],
     [4,5,6]]

B = [[10],
     [20]]

- Perform addition using broadcasting  
- Print the result  
- Explain how broadcasting works across columns  

---

## 69.
Create arrays:
A = np.ones((3,1))
B = np.arange(4)

- Add both arrays using broadcasting  
- Print the result  
- Print shapes of A, B, and result  

---

## 70.
Create a dataset:
data = [[10,20,30],
        [40,50,60]]

- Create a mean array:
[25,35,45]

- Subtract mean from data using broadcasting  
- Print the normalized result  
- Explain why broadcasting is useful here  

---

## 71.
Create a NumPy array:
[1, 2, 3, 4]

- Use `np.square()` to compute square of each element  
- Also compute square using vectorization (`arr * arr`)  
- Print both results  

---

## 72.
Create a NumPy array:
[1, 4, 9, 16]

- Apply `np.sqrt()` to find square roots  
- Print the result  

---

## 73.
Create a NumPy array:
[-5, -3, 2, 4]

- Apply `np.abs()` to get absolute values  
- Print the result  

---

## 74.
Create an array of angles in degrees:
[0, 30, 60, 90]

- Convert them to radians using `np.radians()`  
- Apply `np.sin()`  
- Print the result  

---

## 75.
Using the same angles:
- Apply `np.cos()`  
- Print the result  

---

## 76.
Create a NumPy array:
[1, 2, 3]

- Apply `np.exp()`  
- Print the result  

---

## 77.
Create a NumPy array:
[1, 10, 100]

- Apply:
  - `np.log()`  
  - `np.log10()`  
  - `np.log2()`  
- Print all results  

---

## 78.
Create a NumPy array:
[10, 20, 30]

- Apply comparison functions:
  - `np.greater(arr, 15)`  
  - `np.less(arr, 25)`  
- Print the boolean results  

---

## 79.
Create two boolean arrays:
a = [True, False, True]  
b = [True, True, False]

- Apply:
  - `np.logical_and(a, b)`  
  - `np.logical_or(a, b)`  
  - `np.logical_not(a)`  
- Print all results  

---

## 80.
Create a custom function:
Convert Celsius to Fahrenheit:
F = (C * 9/5) + 32

- Use `np.vectorize()` to apply it on:
  [0, 20, 30]  
- Print the result  

---


## 81.
Create a NumPy array:
[10, 20, 30, 40, 50]

- Calculate the **mean** using `np.mean()`  
- Create a 2D array and calculate mean **along axis=0**  
- Print both results  

---

## 82.
Create two arrays:
[3, 7, 2, 9, 5]  
[1, 2, 3, 4]

- Calculate the **median** for both arrays  
- Explain the difference between odd and even length datasets  

---

## 83.
Create a NumPy array:
[1, 2, 2, 3, 3, 3, 4]

- Find the **mode** using `np.unique()` and `np.argmax()`  
- Print the most frequent value  

---

## 84.
Create a NumPy array:
[10, 12, 14, 16, 18]

- Calculate:
  - Standard deviation using `np.std()`  
  - Variance using `np.var()`  
- Print both results  
- Explain the relationship between variance and standard deviation  

---

## 85.
Create a NumPy array:
[10, 20, 30, 40, 50]

- Calculate:
  - Minimum and maximum values  
  - 25th, 50th, and 75th percentiles  
  - Quantiles (0.25, 0.5, 0.75)  

Then:
- Create two arrays:
  x = [1,2,3,4,5]  
  y = [2,4,6,8,10]  

- Compute **correlation** using `np.corrcoef()`  
- Print the result  

---

## 86.
Create a NumPy array:
[10, 20, 30, 40, 50]

a) Find the total sum of all elements  
b) Compute the sum along axis=0 after reshaping it into a 2×5 matrix (if possible)

---

## 87.
Given the array:
[[1, 2],
 [3, 4],
 [5, 6]]

a) Calculate the product of all elements  
b) Find the product along columns using axis=0  
c) Explain the difference between total product and axis-based product  

---

## 88.
Create a NumPy array:
[2, 4, 6, 8]

a) Compute the cumulative sum using `np.cumsum()`  
b) Compute the cumulative product using `np.cumprod()`  
c) Explain how cumulative operations differ from normal aggregation  

---

## 89.
Given the array:
[15, 3, 22, 7, 10]

a) Find the minimum and maximum values  
b) Find the index of the minimum value using `np.argmin()`  
c) Find the index of the maximum value using `np.argmax()`  
d) Explain what these indices represent  

---

## 90.
Given a 2D array:
[[5, 9, 2],
 [7, 1, 6]]

a) Find the minimum value along axis=0  
b) Find the maximum value along axis=1  
c) Apply `np.argmax()` and explain why it returns a single index  
d) Show how the array is flattened during argmax computation  


## 91.
Create a NumPy array:
[1, 2, 3, 4, 5, 6]

a) Reshape it into a 2×3 matrix  
b) Reshape it into a 3×2 matrix using `-1` for automatic dimension calculation  
c) Explain why total elements must remain constant during reshaping  

---

## 92.
Given the array:
[[1, 2, 3],
 [4, 5, 6]]

a) Flatten the array using `flatten()`  
b) Modify the first element of the flattened array and check if the original array changes  
c) Repeat using `ravel()` and observe the difference  
d) Explain the key difference between `flatten()` and `ravel()`  

---

## 93.
Create a 2D array:
[[10, 20, 30],
 [40, 50, 60]]

a) Transpose the array using `.T`  
b) Write the original and transposed shapes  
c) Explain how rows and columns are interchanged  

---

## 94.
Create a 3D array using:
np.arange(8).reshape(2,2,2)

a) Display the original array shape  
b) Swap axis 0 and axis 2 using `np.swapaxes()`  
c) Explain how the data orientation changes after swapping axes  

---

## 95.
Create a NumPy array:
[1, 2, 3]

a) Expand its dimensions along axis=0 and axis=1 using `np.expand_dims()`  
b) Show the resulting shapes in both cases  
c) Create an array with shape (1,1,3) and use `np.squeeze()`  
d) Explain how `squeeze()` removes dimensions of size 1  

## 96.
Create two 1D NumPy arrays:
[1, 2, 3] and [4, 5, 6]

a) Concatenate them using `np.concatenate()`  
b) Explain what happens when no axis is specified  
c) Compare the result with `np.vstack()`  

---

## 97.
Given two 2D arrays:
[[1, 2],
 [3, 4]]

and

[[5, 6],
 [7, 8]]

a) Concatenate them vertically using `axis=0`  
b) Concatenate them horizontally using `axis=1`  
c) Explain how shape compatibility affects concatenation  

---

## 98.
Create two arrays:
a = [1,2,3]  
b = [4,5,6]

a) Stack them using `np.vstack()`  
b) Stack them using `np.hstack()`  
c) Use `np.column_stack()` and explain how it differs from `hstack()`  
d) Compare `row_stack()` with `vstack()`  

---

## 99.
Given the array:
[1, 2, 3, 4, 5, 6]

a) Split the array into 3 equal parts using `np.split()`  
b) Split the array at indices [2,4]  
c) Explain the difference between equal splitting and index-based splitting  

---

## 100.
Given a 2D array:
[[1, 2, 3, 4],
 [5, 6, 7, 8]]

a) Split the array vertically using `np.vsplit()`  
b) Split the array horizontally using `np.hsplit()`  
c) Explain the difference between row-wise and column-wise splitting  
d) Give a real-world example where splitting arrays is useful  


## 101.
Create a NumPy array:
[5, 2, 8, 1, 3]

a) Sort the array using `np.sort()`  
b) Verify that the original array remains unchanged  
c) Sort the same array using `array.sort()` and observe the difference  
d) Explain the difference between copy-based sorting and in-place sorting  

---

## 102.
Given a 2D array:
[[3, 1, 2],
 [6, 4, 5]]

a) Sort the array row-wise using `axis=1`  
b) Sort the array column-wise using `axis=0`  
c) Explain how sorting along different axes affects the result  

---

## 103.
Create a NumPy array:
[50, 10, 30, 20]

a) Find the indices that would sort the array using `np.argsort()`  
b) Use these indices to sort another array:
names = ["A", "B", "C", "D"]  
c) Explain how `argsort()` is useful in ranking problems  

---

## 104.
Given the array:
[1, 2, 2, 3, 3, 3, 4, 5]

a) Find unique values using `np.unique()`  
b) Find unique values along with their counts  
c) Explain how this can be used to compute frequency of elements  

---

## 105.
Given the sorted array:
[10, 20, 30, 40]

a) Find the insertion index of 25 using `np.searchsorted()`  
b) Find insertion indices for multiple values [5, 15, 35]  
c) Use `np.where()` to find indices where values are greater than 25  
d) Use `np.nonzero()` on [0,1,0,2,3,0] and explain the result  

